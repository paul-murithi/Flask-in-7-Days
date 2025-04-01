from flask import Flask
from .config import Config
from .extensions import db, login_manager
from .blueprints.auth import auth_bp
from .blueprints.posts import posts_bp

# The app factory function that creates the Flask app
def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Load configurations from the Config class
    app.config.from_object(Config)  # Config class (can be Dev or Prod)

    # Initialize extensions like the database and login manager
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints (modularize the app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)

    # Return the app instance
    return app
