from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query = """SELECT products.productID, products.name, products.uom_id, products.pricePerUnit, uom.unit
    FROM groceryStore.products
    INNER JOIN groceryStore.uom ON products.uom_id = uom.uom_id"""

    cursor.execute(query)

    response = []

    for(productID, name, uom_id, pricePerUnit, unit) in cursor:
        response.append({
            "productID": productID,
            "name": name,
            "uom_id": uom_id,
            "pricePerUnit": pricePerUnit,
            "unit": unit
        })


    return response;

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = """INSERT INTO groceryStore.products (name, uom_id, pricePerUnit) VALUES (%s, %s, %s)"""

    data = (product['name'], product['uom_id'], product['pricePerUnit'])

    cursor.execute(query, data);
    connection.commit();
    return cursor.lastrowid;

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM groceryStore.products WHERE productID =" +str(product_id)
    cursor.execute(query);
    connection.commit();

if __name__ == "__main__":
    connection = get_sql_connection()
    print(delete_product(connection, 11))