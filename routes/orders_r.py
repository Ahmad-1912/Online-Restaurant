from flask import request, jsonify, Blueprint, render_template, session
from datetime import datetime
import pytz
from elements.orders import OrderItem, Orders, orders_bp
from config.define import DB

db = DB

# POST for Orders
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400  # Bad Request

    # Get customerID from session
    customerID = session.get('cID')  # Use session.get() to get cID from customer_r route
    if customerID is None:
        return jsonify({"message": "User not logged in"}), 401  # Unauthorized
    
    # Get orderItems from data
    orderItems = data.get('orderItems')
    if not orderItems:
        return jsonify({"message": "No order items provided"}), 400  # Bad Request
    
    # Get PaymentMethod from data
    paymentMethod = data.get('paymentMethod')
    if not paymentMethod:
        return jsonify({"message": "No paymentMethod provided"}), 400

    # Set default orderStatus to 'Placed'
    orderStatus = 'placed'

    # Specify the timezone
    timezone = pytz.timezone('Europe/Berlin')
    # Get the current time in the specified timezone
    current_time_in_timezone = datetime.now(timezone)

    # Create a new order
    order = Orders(customerID=customerID, orderStatus=orderStatus, orderDate=current_time_in_timezone, paymentMethod=paymentMethod)
    # Add the new order to the session and commit to generate orderID
    db.session.add(order)
    db.session.commit()
    
    # Create OrderItem instances and add them to the order
    for item in orderItems:
        order_item = OrderItem(orderID=order.orderID, itemID=item['itemID'], quantity=item['quantity'])
        # Add the new order to the session
        db.session.add(order_item)

    # Commit the session to save the changes
    db.session.commit()

    # Return a success message
    return jsonify({"message": "Order created successfully"}), 201  # Created
