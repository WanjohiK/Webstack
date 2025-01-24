from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

print("Template folder path:", os.path.join(os.getcwd(), 'app', 'templates'))

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirect to login page when needed

    # Define the user_loader function
    @login_manager.user_loader
    def load_user(user_id):
        # Import the User model here to avoid circular imports
        from app.models import User
        return User.query.get(int(user_id))  # Retrieve the user based on the user_id stored in the session

    # Import blueprints
    from app.routes import auth, main

    # Register blueprints
    app.register_blueprint(auth, url_prefix='/auth')  # Authentication routes will be prefixed with /auth
    app.register_blueprint(main)  # Main routes (home) will be accessible without a prefix

    return app
