from app import create_app
import config


flask_app = create_app(config.app_config["development"])

if __name__ == "__main__":
    flask_app.run()
else:
    application = flask_app