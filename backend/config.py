import os


class Config():
    TEMPLATE_FOLDER = os.getcwd() + "/dist"
    STATIC_FOLDER = os.getcwd() + "/dist/static/"
    API_KEY = os.environ["API_KEY"]
    AUTHDOMAIN = os.environ["AUTHDOMAIN"]
    DBURL = os.environ["DBURL"]
    PROJECT_ID = os.environ["PROJECT_ID"]
    STORE_BUCKET = os.environ["STORE_BUCKET"]
    MSG_SENDER_ID = os.environ["MSG_SENDER_ID"]
    APPID = os.environ["APPID"]
    MEASURE_ID = os.environ["MEASURE_ID"]


class DevelopmentConfig(Config):
    """ Development Specific Config """
    DEBUG = True


class ProductionConfig(Config):
    """ Production Specific Config """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}