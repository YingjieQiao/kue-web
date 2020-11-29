import os


class Config():
    TEMPLATE_FOLDER = os.getcwd() + "/dist"
    STATIC_FOLDER = os.getcwd() + "/dist/static/"
    API_KEY = os.environ.get("API_KEY")
    AUTHDOMAIN = os.environ.get("AUTHDOMAIN")
    DBURL = os.environ.get("DBURL")
    STORE_BUCKET = os.environ.get("STORE_BUCKET")
    MSG_SENDER_ID = os.environ.get("MSG_SENDER_ID")
    APPID = os.environ.get("APPID")
    MEASURE_ID = os.environ.get("MEASURE_ID")


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