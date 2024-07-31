from flask import Flask         # Marco de trabajo principal de la app
from flask_sqlalchemy import SQLAlchemy  # Biblioteca para la interaccion con la base de datos
from flask_migrate import Migrate  # Extension que permite manejar las migraciones de la base de datos
from flask_login import LoginManager
from app.extensions import db, migrate, login_manager
"""
instanciamos SQLAlchemy y Migrate, que luego seran vinculadas a la app
flask
"""

# definir la funcion create_app


def create_app(config_class='app.config.Config'):

    """
    Esta función se usa para crear y configurar una instancia
    de la aplicacion Flask. Permite una configuracion flexible y reutilizable
    :param config_class:
    :return: instancia de la app
    """

    app = Flask(__name__)       # se crea una instancia de Flask
    app.config.from_object(config_class)    # la configuracion de la app se carga desde la clase de configuracion

    """
        Inicializar SQLAlchemy y Migrate con la app:
    """

    db.init_app(app)        # vincula la instancia SQLAlchemy con la app flask
    migrate.init_app(app, db) # vincula la instancia Migrate con la app flask y con la instancia SQLAlchemy para manejar migraciones
    login_manager.init_app(app)

    # Registrar blueprints
    from app.models import User
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # redirige a la pagina de login si el usuario no esta autenticado
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'


    return app  # retorna instancia de la app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))