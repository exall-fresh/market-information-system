import mysql.connector as db

def db_conn():
    connection = db.connect(user="root", database="mis-python")
    cursor = connection.cursor()
    return cursor, connection