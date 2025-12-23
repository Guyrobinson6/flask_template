from flask import Flask
from config import config_map # Import the map, not just the class
from .extensions import db, bootstrap

# Default to 'development' if no argument is provided
def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load the correct config class based on the name
    app.config.from_object(config_map[config_name])

    # Initialize Flask extensions
    db.init_app(app)
    bootstrap.init_app(app)

    # Register Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app