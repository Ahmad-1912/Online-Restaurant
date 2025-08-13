#To recognize imports from directory
import os, sys
cwd=os.getcwd() # Get the current working directory
sys.path.insert(0, cwd) #Insert the current working directory into sys.path
###

from flask import request, Blueprint, jsonify, redirect, url_for, render_template, session, flash

from elements.admin import  Admin, admin_bp
from elements.customers import Customer
from elements.menu import Menu
from elements.orders import Orders, OrderItem
from config.define import DB,APP

db=DB
app=APP

# Route for login form
@admin_bp.route('/login/admin', methods=['POST'])
def login_admin():
    username = request.form.get('identifier')
    password = request.form.get('password')
    user = Admin.query.filter_by(username=username).first()
    if user and user.password == password:
        session['ID'] = user.adminID
        return redirect(url_for('admin.view_all_orders'))
    else:
        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('main'))  

# Route to view all orders
@admin_bp.route('/admin_orders', methods=['GET', 'POST'])
def view_all_orders():
    if request.method == 'POST':
        # Handle order status update
        orderID = request.form.get('orderID')
        new_status = request.form.get('newStatus')
        if orderID and new_status:
            order = Orders.query.get(orderID)
            order.orderStatus = new_status
            db.session.commit()
            flash('Order status updated successfully.', 'success')
            return redirect(url_for('admin.view_all_orders'))
    
    # Handle view all orders (GET request)
    all_orders = Orders.query.all()
    # Fetch menu items from the database
    menu_items = Menu.query.all()
    # Create a dictionary mapping item IDs to item names
    menu = {item.itemID: item.itemName for item in menu_items}
    return render_template('admin_orders.html', orders=all_orders, menu=menu)


# Route to view all and edit menu
@admin_bp.route('/admin_menu', methods=['GET', 'POST'])
def admin_menu():
    if request.method == 'POST':
        # Handle the form submission for updating menu items
        itemID = request.form.get('itemID')
        new_price = request.form.get('new_price')
        new_availability = request.form.get('new_availability') == 'True'

        if itemID:
            item = Menu.query.get(itemID)
            if item:
                # Update price only if a new price is provided
                if new_price:
                    item.price = new_price
                # Always update availability
                item.availability = new_availability
                db.session.commit()
                flash('Menu item updated successfully.', 'success')
        else:
            flash('Update failed', 'error')
        return redirect(url_for('admin.admin_menu'))

    # Handle the GET request to display menu items
    menu_items = Menu.query.all()
    return render_template('admin_menu.html', items=menu_items)
