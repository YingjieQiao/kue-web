from .app import create_app
import config


flask_app = create_app(config.app_config["development"])
