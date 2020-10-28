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
def get_order():
    """
    TODO:  pushing the order into db should be done in the Java App
    Payload format:
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
        },

        "eta": "NA"
    }

    query (in python): db.child(data["dtype"]).child(data["sn"]).push(data["payload"])
    """

    record = db.child('orders').get().val()
    last_record = list(record[-1].values())

    response = {
        "data": last_record[0]["eta"]
    }
    return jsonify(response)


@pages.route('/')  
def home():
    return render_template("index.html")


@pages.route('/<int:order_id>')  
#TODO: encrypt order_id to a randomized sequence (like Isd8@%G) later
def customer(order_id):
    return render_template("customer.html")

