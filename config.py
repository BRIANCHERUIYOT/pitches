class Config:
    """
    parent configurations class
    """

    SECRET_KEY = "brian"
    DEBUG = True

class Prodconfig(Config):
    """
    production cofiguration
    """


class DevConfig(Config):
    """
    Development configuration
    """
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':Prodconfig,
}