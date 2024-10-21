import os

class Settings:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./sleep.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta')

settings = Settings()