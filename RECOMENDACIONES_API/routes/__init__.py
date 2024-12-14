from flask import Flask, Blueprint

# Crear blueprints
favoritos_bp = Blueprint('favoritos', __name__)
tendencias_bp = Blueprint('tendencias', __name__)
visualizaciones_bp = Blueprint('visualizaciones', __name__)

# Importar las vistas asociadas a los blueprints
from . import favoritos, tendencias, visualizaciones

def create_app():
    # Crear la instancia de Flask
    app = Flask(__name__)

    # Registrar los blueprints
    app.register_blueprint(favoritos_bp, url_prefix='/favoritos')
    app.register_blueprint(tendencias_bp, url_prefix='/tendencias')
    app.register_blueprint(visualizaciones_bp, url_prefix='/visualizaciones')

    return app
