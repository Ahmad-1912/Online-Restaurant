# To recognize imports from directory
import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
#
from flask import Flask, render_template, session

#
from config.define import DB, APP

from routes.menu_r import menu_bp
from routes.orders_r import orders_bp
from routes.customers_r import customers_bp
from routes.admin_r import admin_bp

APP.register_blueprint(menu_bp)
APP.register_blueprint(orders_bp)
APP.register_blueprint(customers_bp)
APP.register_blueprint(admin_bp)

#
@APP.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@APP.route('/')
def main():
    return render_template('main.html')

# Run the app
if __name__ == '__main__':
    APP.run(debug=True)
