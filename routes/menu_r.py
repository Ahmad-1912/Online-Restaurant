import os, sys
cwd = os.getcwd()  # Get the current working directory
sys.path.insert(0, cwd)  # Insert the current working directory into sys.path
###

from flask import request, jsonify, Blueprint, render_template
from elements.menu import Menu, menu_bp

# Render menu page
@menu_bp.route('/menu', methods=['GET'])
def get_menu_page():
    items = Menu.query.all()
    return render_template('menu.html', items=items)

# Render view-only menu page
@menu_bp.route('/menu_view', methods=['GET'])
def get_menu_view_page():
    items = Menu.query.all()
    return render_template('menu_view.html', items=items)
