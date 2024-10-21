from flask import Flask
from app.core.config import Config
from app.db.session import init_db
from app.api.endpoints import sleep

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    init_db(app)

    app.register_blueprint(sleep.bp, url_prefix='/sleep')
    
    return app