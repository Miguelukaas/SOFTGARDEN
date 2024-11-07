from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Importar configuración de `config.py`
    
    # Registrar blueprints u otras configuraciones si es necesario
    from .views.main_view import main_bp
    app.register_blueprint(main_bp)
    
    return app
