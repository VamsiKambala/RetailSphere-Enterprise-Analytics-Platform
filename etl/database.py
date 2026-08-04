import mysql.connector

from config import (MYSQL_CONFIG)

def get_connection(
        database_name:str
):
    connection=mysql.connector.connect(
        host=MYSQL_CONFIG["host"],
        user=MYSQL_CONFIG["user"],
        password=MYSQL_CONFIG["password"],
        port=MYSQL_CONFIG["port"],
        database=database_name
    )
    return connection