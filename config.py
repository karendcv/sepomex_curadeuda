import os

class Config:
    DEBUG = True
    DEVELOPMENT = True

class DevelopmentConfig(Config):    
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

config = {
    'development': DevelopmentConfig,
}
