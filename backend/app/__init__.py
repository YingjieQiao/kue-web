from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import *
import requests


def create_app(Config):
    app = Flask(__name__)
    CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.static_folder = app.config["STATIC_FOLDER"]
    app.template_folder = app.config["TEMPLATE_FOLDER"]

    with app.app_context():
        from app.apis.routers import apis
        app.register_blueprint(apis)

    return app


