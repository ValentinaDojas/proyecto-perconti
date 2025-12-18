import mysql.connector
import configparser

def conectar():
    config = configparser.ConfigParser()
    config.read("config.ini")

    return mysql.connector.connect(
        host=config["database"]["host"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["database"]
    )
