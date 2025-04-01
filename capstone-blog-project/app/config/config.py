import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    DEBUG = False  # Default to False for safety

class DevelopmentConfig(Config):
    """Development-specific configuration."""
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    """Production-specific configuration."""
    FLASK_ENV = 'production'
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration."""
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory DB for tests
