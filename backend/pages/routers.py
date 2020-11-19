from flask import Blueprint, render_template, current_app, jsonify, request
import logging
from random import randint
import pyrebase
import os, sys

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


@pages.route('/api/getOrder', methods=["GET", "POST"])
def get_order():
    """
    query (in python): db.child(data["dtype"]).child(data["sn"]).push(data["payload"])
    1. pyrebase
    2. get username from Vue -- how? url? 
    3. change text: waiting for xxx seconds / Done go collect
    qns:
    1. replace localhost with IP?

    """

    data = request.get_json()
    #print("\n")
    #print(data)
    #print(data["username"])
    # {'order_id': '123', 'username': 'ss'}
    #print("\n")

    path = "accounts/"+data["username"]+"/order_web"
    order_web = db.child(path).get().val()

    target_order = {}
    for each_order in order_web.values():
        if (data["order_id"] == each_order["orderID"]):
            target_order = each_order
            break

    print(target_order["finishTime"])
        
    response = {
        "order time": target_order["orderTime"],
        "finish time": target_order["finishTime"]
    }
    return jsonify(response)


@pages.route('/')  
def home():
    return render_template("index.html")


@pages.route('/<int:order_id>')  
#TODO: encrypt order_id to a randomized sequence (like Isd8@%G) later
def customer(order_id):
    return render_template("customer.html")

