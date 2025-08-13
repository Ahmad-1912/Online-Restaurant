# To recognize imports from directory
import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
#
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import inspect
import sqlite3

# Create the Flask application instance
APP = Flask(__name__, template_folder='../templates', static_folder='../static')
# Set the secret key
APP.secret_key = 'app_secret_key'

# Configure the SQLite database URI
# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Get the parent directory
parentdir = os.path.dirname(basedir)
# Use the parent path (project absolute path) in the SQLite URI
db_path = os.path.join(parentdir, 'DB', 'OnlineResturantX.sqlite')
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

# Print the path to the SQLite database file
print("Path to the SQLite database file: ", db_path)

# Initialize the SQLAlchemy extension
DB = SQLAlchemy(APP)

