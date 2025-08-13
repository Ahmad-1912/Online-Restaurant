# To recognize imports from directory
import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
#
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, request

from config.define import DB

db = DB

customers_bp = Blueprint('customers', __name__)

class Customer(db.Model):
    __tablename__ = 'Customer'
    customerID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # relatiionship to Orders (to access all orders of certain costumer)
    orders = db.relationship('Orders', backref='customer', lazy=True)
    # to convert items to JSON
    def Costumer_to_dict(self):
        return {
            'customerID': self.customerID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'address': self.address
        }

# Functions for passwords
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
