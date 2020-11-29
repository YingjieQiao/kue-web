from flask import Blueprint, render_template, current_app, jsonify, request
import logging
from random import randint
import pyrebase
import os, sys

pages = Blueprint('pages', __name__, template_folder=current_app.config["TEMPLATE_FOLDER"])

# use firebase for prototyping
# env var later
firebase_config = {
    "apiKey": current_app.config["APIKEY"],
    "authDomain": current_app.config["AUTHDOMAIN"],
    "databaseURL": current_app.config["DBURL"],
    "projectId": current_app.config["PROJECT_ID"],
    "storageBucket": current_app.config["STORE_BUCKET"],
    "messagingSenderId": current_app.config["MSG_SENDER_ID"],
    "appId": current_app.config["APP_ID"],
    "measurementId": current_app.config["MEASURE_ID"]
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

