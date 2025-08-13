# To recognize imports from directory
import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
#

from flask import Blueprint, jsonify, request

from config.define import DB

db = DB

orders_bp = Blueprint('orders', __name__)

class OrderItem(db.Model):
    __tablename__ = 'orderItem'
    orderID = db.Column(db.Integer, db.ForeignKey('Orders.orderID'), primary_key=True)
    itemID = db.Column(db.Integer, db.ForeignKey('Menu.itemID'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order = db.relationship('Orders', back_populates='orderItems')  # Corrected here

class Orders(db.Model):
    __tablename__ = 'Orders'
    orderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.customerID'), nullable=False)
    orderItems = db.relationship('OrderItem', back_populates='order')  # Corrected here
    orderStatus = db.Column(db.String(255), nullable=False)
    orderDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    paymentMethod = db.Column(db.String(255), nullable=False) 

    def orders_to_dict(self):
        return {
            'orderID': self.orderID,
            'customerID': self.customerID,
            'orderStatus': self.orderStatus,
            'orderDate': self.orderDate.isoformat() if self.orderDate else None,
            'PaymentMethod': self.paymentMethod,
            'orderItems': [
            {
                'itemID': item.itemID,
                'quantity': item.quantity
            } for item in self.orderItems
        ]
        }