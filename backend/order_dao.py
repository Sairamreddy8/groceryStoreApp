from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = """INSERT INTO groceryStore.orders (customerName, total, dateTime)
    VALUES(%s, %s, %s)"""

    order_data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(order_query, order_data)
    
    order_id = cursor.lastrowid

    order_details_query = """INSERT INTO groceryStore.order_details (orderID, productID, quantity, totalPrice)
    VALUES(%s, %s, %s, %s)"""
    order_details_data = []

    for order_detail in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail['productID']),
            float(order_detail['quantity']),
            float(order_detail['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = """SELECT * FROM groceryStore.orders"""
    cursor.execute(query)
    response = []

    for(orderID, customerName, total, datetime ) in cursor:
        response.append({
            'orderID': orderID,
            'customerName': customerName,
            'total': total,
            'datetime': datetime
        })

    return response;
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_orders(connection))
    