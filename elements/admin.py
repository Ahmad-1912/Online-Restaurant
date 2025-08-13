# To recognize imports from directory 
import os,sys
cwd= os.getcwd() #Get cuurent working directory
sys.path.insert(0, cwd)
#
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, request

from config.define import DB

db=DB 

admin_bp = Blueprint('admin', __name__)

class Admin(db.Model):
    __tablename__='Admin'
    adminID=db.Column(db.Integer,primary_key=True, autoincrement=True)
    username=db.Column(db.String(255),nullable=False, unique=True)
    password=db.Column(db.String(255),nullable=False)
    admin_rights=db.Column(db.Boolean,nullable=False)

#to convert items to JSON

def Admin_to_dict(self):
    return {
        'adminID': self.adminID,
        'username':self.username,
        'admin_rights': self.admin_rights    
    }

#Functions for password
  
def set_password(self, password):
      self.password = generate_password_hash(password)

def check_password(self,password):
      return check_password_hash(self.password, password)
