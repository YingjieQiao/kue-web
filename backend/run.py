from backend.app import create_app
from backend import config

flask_app = create_app(config.app_config["development"])

if __name__ == "__main__":
    flask_app.run()