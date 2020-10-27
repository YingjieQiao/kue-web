from flask import Blueprint, render_template, current_app, jsonify
import requests
from random import randint


pages = Blueprint('pages', __name__, template_folder="/Users/yingjieqiao/Desktop/kue-web/dist")


@pages.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@pages.route('/', defaults={'path': ''})
@pages.route('/<path:path>')
def catch_all(path):
    if current_app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
