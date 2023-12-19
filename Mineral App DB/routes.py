from flask import Blueprint, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Mineral, Feedback,user_favorites

bp = Blueprint('api', __name__)

# History
@bp.route('/history', methods=['GET'])
@login_required
def history():
    user_id = current_user.id
    user_minerals = Mineral.query.filter_by(user_id=user_id).all()

    minerals_data = [
        {
            'id': mineral.id,
            'name': mineral.name,
            'image_data': mineral.image_data
        }
        for mineral in user_minerals
    ]

    return jsonify({'minerals': minerals_data})

# Add favorite
@bp.route('/favorite/<int:mineral_id>', methods=['POST'])
@login_required
def add_favorite(mineral_id):
    mineral = Mineral.query.get(mineral_id)

    if not mineral:
        return jsonify({'error': 'Mineral not found.'}), 404

    current_user.favorite_minerals.append(mineral)
    db.session.commit()

    return jsonify({'message': 'Mineral added to favorites successfully.'})

# Remove favorite
@bp.route('/unfavorite/<int:mineral_id>', methods=['POST'])
@login_required
def remove_favorite(mineral_id):
    mineral = Mineral.query.get(mineral_id)

    if not mineral:
        return jsonify({'error': 'Mineral not found.'}), 404

    current_user.favorite_minerals.remove(mineral)
    db.session.commit()

    return jsonify({'message': 'Mineral removed from favorites successfully.'})

# Show favorites
@bp.route('/favorites', methods=['GET'])
@login_required
def favorites():
    user_id = current_user.id
    favorite_minerals = Mineral.query.join(user_favorites).filter_by(user_id=user_id).all()

    # Favori minerallerin sadece image_data bilgisini dön
    favorite_minerals_data = [
        {
            'id': mineral.id,
            'image_data': mineral.image_data,
        }
        for mineral in favorite_minerals
    ]

    return jsonify({'minerals': favorite_minerals_data})

# Give feedback
@bp.route('/add_feedback', methods=['POST'])
@login_required
def add_feedback():
    data = request.get_json()

    if 'content' not in data:
        return jsonify({'error': 'Content is required.'}), 400

    new_feedback = Feedback(content=data['content'], user_id=current_user.id)
    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({'message': 'Feedback added successfully.'})

# Login
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required.'}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'error': 'Login failed. Check your username and password.'}), 401

# Signup
@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'All fields are required.'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username is already taken. Please choose another one.'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Signup successful! You can now log in.'})

# Logout 
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    
    return jsonify({'message': 'Logout successful!'})