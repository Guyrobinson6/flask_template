from flask import Flask
from config import Config
from .extensions import db, bootstrap

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    bootstrap.init_app(app)

    # Register Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create database tables automatically within app context
    with app.app_context():
        db.create_all()

    return app