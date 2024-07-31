import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:nM1258menMa@localhost/login_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False