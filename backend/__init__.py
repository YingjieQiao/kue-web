from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests


def create_app():
    app = Flask(__name__,
                static_folder = "/Users/yingjieqiao/Desktop/kue-web/dist/static",
                template_folder = "/Users/yingjieqiao/Desktop/kue-web/dist")
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from backend.pages.routers import pages
    app.register_blueprint(pages)

    return app


