from flask import Flask
import os


def create_app():

    app = Flask(__name__)

    app.config.from_mapping(
        PASSWORD_KEY = os.environ.get('PASSWORD_KEY'),
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )

    from . import db 
    db.init_app(app)
    
    from . import mail 
    app.register_blueprint(mail.bp)

    return app