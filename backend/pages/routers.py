from flask import Blueprint, render_template, current_app, jsonify, request
import logging
from random import randint
import pyrebase
import os, sys

pages = Blueprint('pages', __name__, template_folder=current_app.config["TEMPLATE_FOLDER"])

# use firebase for prototyping
# env var later
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


@pages.route('/api/getOrder', methods=["GET", "POST"])
def get_order():
    """
    qns:
    1. replace localhost with IP?
    """

    data = request.get_json()

    path = "accounts/"+data["username"]+"/order_web"
    order_web = db.child(path).get().val()

    target_order = {}
    for each_order in order_web.values():
        if (data["order_id"] == each_order["orderID"]):
            target_order = each_order
            break

    eta = ""
    if target_order["finishTime"] == -1:
        eta = "Your order is not done yet. Expected waiting time: " + "____" # target_order["ETA"]
    else:
        eta = "Your order is done!"
        
    response = {
        "order time": target_order["orderTime"],
        "eta": eta
    }
    return jsonify(response)


@pages.route('/')  
def home():
    return render_template("index.html")

