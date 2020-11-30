from flask import Blueprint, render_template, current_app, jsonify, request
import logging
from random import randint
import pyrebase
import os, sys

pages = Blueprint('pages', __name__, template_folder=current_app.config["TEMPLATE_FOLDER"])

firebase_config = {
    "apiKey": current_app.config["API_KEY"],
    "authDomain": current_app.config["AUTHDOMAIN"],
    "databaseURL": current_app.config["DBURL"],
    "projectId": current_app.config["PROJECT_ID"],
    "storageBucket": current_app.config["STORE_BUCKET"],
    "messagingSenderId": current_app.config["MSG_SENDER_ID"],
    "appId": current_app.config["APPID"],
    "measurementId": current_app.config["MEASURE_ID"]
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


@pages.route('/api/getOrder', methods=["GET", "POST"])
def get_order():
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
        eta = "Your order is not done yet. Expected waiting time: " + str(target_order["eta"]) + " minutes"
    else:
        eta = "Your order is done!"
        
    response = {
        "order time": target_order["orderDate"],
        "eta": eta
    }
    return jsonify(response)


@pages.route('/api/postRating', methods=["GET", "POST"])
def postRating():
    data = request.get_json()

    path = "accounts/"+data["username"]+"/order_web"
    order_web = db.child(path).get().val()

    # target_order = {}
    target_key = ""
    for key, value in order_web.items():
        if (data["order_id"] == value["orderID"]):
            target_order = value
            target_key = key

    if target_key == "":
        return "done"

    db.child(path).child(target_key).update({"rating": data["rating"]})
    return "done"

@pages.route('/')  
def home():
    return render_template("index.html")

