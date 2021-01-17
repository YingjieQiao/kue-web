from app import create_app
from app.config import app_config


application = create_app(app_config["development"])

if __name__ == "__main__":
    application.run()
