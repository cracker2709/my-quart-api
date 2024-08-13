import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    ENV_PROP = "None"

    ENV_TYPE_ID_DICT = {
        "a": "staging",
        "p": "production",
        "r": "op",
        "q": "sit",
        "d": "development"
    }
    VAULT_ENV_TYPE_SHORTNAME_DICT = {
        "a": "pp",
        "p": "prod",
        "r": "op",
        "q": "sit",
        "d": "dev"
    }

    ENV = "ENV"
    APP_PATH = "app/"

class DevelopmentConfig(Config):
    DEBUG = True
    ENV_PROP = "Dev"
    PORT = os.getenv('SERVER_PORT', 5000)
    HOST = os.getenv('SERVER_HOST', "127.0.0.1")


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV_PROP = "Test"
    LIVESERVER_PORT = 0
    PORT = os.getenv('SERVER_PORT', 5000)
    HOST = os.getenv('SERVER_HOST', "127.0.0.1")


class ProductionConfig(Config):
    DEBUG = False
    ENV_PROP = "Prod"
    PORT = os.getenv('SERVER_PORT', 5000)
    HOST = os.getenv('SERVER_HOST', "0.0.0.0")


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
