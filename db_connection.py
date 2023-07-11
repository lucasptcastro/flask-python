import mysql.connector
from mysql.connector import errorcode 
from environment.env import Environment

environment = Environment()

class DbConnection:
    def __init__(self):
        self.HOST = environment.get_env("HOST")
        self.USER = environment.get_env("USER")
        self.PASSWORD = environment.get_env("PASSWORD")
        self.DATABASE = environment.get_env("DATABASE") 
    
    def connect(self):
        try:
            db_connection = mysql.connector.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, database=self.DATABASE)
            print("Database connected!")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist!")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username or password incorrect!")
            else:
                print(f"Erro! {error}")
        else:
            db_connection.close()


DbConnection().connect()