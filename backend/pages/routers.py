from flask import Blueprint, render_template, current_app, jsonify
import requests
from random import randint
import pyrebase
import os

pages = Blueprint('pages', __name__, template_folder=current_app.config["TEMPLATE_FOLDER"])

# use firebase for prototyping
firebase_config = {
    "apiKey": "AIzaSyBF_J7wH5PNs_T2-C89qvybopm6pid8Dk8",
    "authDomain": "kueapp-722a3.firebaseapp.com",
    "databaseURL": "https://kueapp-722a3.firebaseio.com",
    "projectId": "kueapp-722a3",
    "storageBucket": "kueapp-722a3.appspot.com",
    "messagingSenderId": "12190067463",
    "appId": "1:12190067463:web:832bf28c6b4c075001f3a2",
    "measurementId": "G-CN12N924W5"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


@pages.route('/api/random')
def random_number():
    # this API should be in the Java App in the end
    count = db.child("count").get().val()
    count += 1
    db.child("count").set(count)

    data = {
        "dtype" : "orders",

        "sn": count,

        "payload" : {
            "food1": "Big Mac",
            "food2": "fries",
            "food3": "code",
            "food4": None,
            "food5": None,
            "food6": None,
            "food7": None,
            "food8": None,
            "food9": None,
            "food10": None
        }
    }
    db.child(data["dtype"]).child(data["sn"]).push(data["payload"])

    # try getting last record
    # last_record = db.child(data["dtype"]).order_by_key().limit_to_last(1).get().val()
    # print(last_record)

    response = {
        "data": data
    }
    return jsonify(response)


@pages.route('/')
#@pages.route('/<path:path>')
def catch_all():
    return render_template("index.html")

