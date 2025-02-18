from flask import Flask
from flask_cors import CORS 
from flaskr.config import Config
from flaskr.routes.stats_routes import stats_bp  

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config) 

    CORS(app) 


    app.register_blueprint(stats_bp, url_prefix="/api/stats")

    return app
