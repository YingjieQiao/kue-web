from app import db
from flask import current_app


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    orders = db.relationship('Order', backref='author', lazy=True)  # one to many

    def __repr__(self):
        return '<Restaurant {}>'.format(self.username)    


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    finishTime = db.Column(db.Integer)
    eta = db.Column(db.Integer)
    orderID = db.Column(db.String(128), index=True, unique=True)
    orderDate = db.Column(db.String(128))
    orderTime = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    food = db.Column(db.String(128))  # "food1, food2, food3", use split(',')

    def __repr__(self):
        return '<Order {}>'.format(self.orderID)    


