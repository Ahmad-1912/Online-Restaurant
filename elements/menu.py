# To recognize imports from directory
import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
#

from flask import Blueprint, jsonify, request

from config.define import DB

db = DB

menu_bp = Blueprint('menu', __name__)

class Menu(db.Model):
    __tablename__ = 'Menu'
    itemID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    itemName = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    availability = db.Column(db.Boolean, nullable=False)
    # to convert items to JSON
    def menu_to_dict(self):
        return {
            'itemID': self.itemID,
            'itemName': self.itemName,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'availability': self.availability
        }
