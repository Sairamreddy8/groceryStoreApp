from flask import Flask, request, jsonify
import json
from product_Dao import get_all_products, insert_new_product, delete_product
from uom_dao import get_uoms
from order_dao import insert_order, get_all_orders
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])

def get_products():
    products = get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])

def deleteProduct():
    return_id = delete_product(connection, request.form['productID'])
    response = jsonify({
        'productID' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])

def get_uom():
    response = get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])

def insertProduct():
    request_payload = json.loads(request.form['data'])
    product_id = insert_new_product(connection, request_payload)
    response = jsonify({
        'productID' : product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])

def insertOrder():
    request_payload = json.loads(request.form['data'])
    order_id = insert_order(connection, request_payload)
    response = jsonify({
        'orderID' : order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])

def get_orders():
    orders = get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting server")
    app.run(port=5000)