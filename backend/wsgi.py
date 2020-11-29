from backend.app import create_app
from backend import config


application = create_app(config.app_config["development"])

if __name__ == "__main__":
    application.run()
