from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import requests

app = Flask(__name__)
db = SQLAlchemy(app)


def create_app(config):
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config)


    app.static_folder = app.config["STATIC_FOLDER"]
    app.template_folder = app.config["TEMPLATE_FOLDER"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from app.apis.routes import api
        app.register_blueprint(api)

    return app


