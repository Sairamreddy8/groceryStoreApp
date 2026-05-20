import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Qpzmg@123',
                                        host='127.0.0.1',
                                        database='groceryStore')
    # print("Connected to MySQL database")
    return __cnx