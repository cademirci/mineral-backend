from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_favorites = db.Table(
    'user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('mineral_id', db.Integer, db.ForeignKey('mineral.id'), primary_key=True)  
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    minerals = db.relationship('Mineral', backref='user', lazy=True)
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)

    # Favori mineral (resim) ilişkisi
    favorite_images = db.relationship('Mineral', secondary=user_favorites, backref='favorited_by')  

    # Kullanıcının çektiği resimlerin ilişkisi
    images = db.relationship('Mineral', backref='user') 

class Mineral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship('User', backref='minerals', lazy=True)
    favorited_by = db.relationship('User', secondary=user_favorites, backref='favorite_images')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship('User', backref='feedbacks', lazy=True)