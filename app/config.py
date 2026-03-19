import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devnetsecret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:root@db/chatdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False