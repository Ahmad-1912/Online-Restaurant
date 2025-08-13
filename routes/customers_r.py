from flask import request, Blueprint, jsonify, redirect, url_for, render_template, session, flash
from elements.customers import Customer, customers_bp
from elements.orders import Orders 
from elements.menu import Menu
from config.define import DB

db = DB

# Route for registration form
@customers_bp.route('/register', methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    address = request.form['address']
    password = request.form['password']

    # Check if email already exists
    if Customer.query.filter_by(email=email).first() is not None:
        flash('An account with this email allready exists. Please use another one.', 'error')
        return jsonify({"message": "Email already exists!"}), 400

    # Create new customer
    new_customer = Customer(firstName=firstName, lastName=lastName, email=email, address=address, password=password)
    
    db.session.add(new_customer)
    db.session.commit()

    return redirect(url_for('customers.customer_orders', customerID=new_customer.customerID))

# Route for login form
@customers_bp.route('/login/customer', methods=['POST'])
def login_customer():
    email = request.form.get('identifier')
    password = request.form.get('password')
    user = Customer.query.filter_by(email=email).first()
    if user and user.password == password:
        session['cID'] = user.customerID
        return redirect(url_for('customers.customer_orders', customerID=user.customerID))
    else:
        flash('Invalid email or password. Please try again.', 'error')
        return redirect(url_for('main'))  

# Route to show orders for the specific customer
@customers_bp.route('/customer/orders/<int:customerID>', methods=['GET'])
def customer_orders(customerID):
    customer_orders = Orders.query.filter_by(customerID=customerID).all()
    customer = Customer.query.get(customerID) #define customer 

    # Fetch menu items from the database
    menu_items = Menu.query.all()
    # Create a dictionary mapping item IDs to item names
    menu = {item.itemID: item.itemName for item in menu_items}

    return render_template('order.html', orders=customer_orders, customer=customer, menu=menu)
