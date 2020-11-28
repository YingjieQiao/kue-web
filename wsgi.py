#from backend import create_app
from config import Config
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

def create_app(Config):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.static_folder = app.config["STATIC_FOLDER"]
    app.template_folder = app.config["TEMPLATE_FOLDER"]

    with app.app_context():
        from backend.pages.routers import pages
        app.register_blueprint(pages)

return app

app = create_app(Config)