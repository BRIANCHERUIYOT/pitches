import os
class Config:
    """
    parent configurations class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitcheses'
    SECRET_KEY = "brian"
    
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class Prodconfig(Config):
    """
    production cofiguration
    """
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    """
    Development configuration
    """
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitcheses'
    SECRET_KEY = "brian"
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':Prodconfig,
}