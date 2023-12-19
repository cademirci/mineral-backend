from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db
from routes import bp

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MineralApp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Kullanıcı girişi yapmadan önce yönlendirilecek sayfanın adı

    with app.app_context():
        db.create_all()
    
   
    app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)