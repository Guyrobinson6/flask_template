import os
from dotenv import load_dotenv

# Load variables from .env file (if present)
load_dotenv()


class Config:
    """Base configuration shared across all environments."""

    # Secret key for sessions, CSRF, etc.
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Settings for local development."""
    DEBUG = True


class ProductionConfig(Config):
    """Settings for production deployment."""
    DEBUG = False


# Used by create_app() in app/__init__.py
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}