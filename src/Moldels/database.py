import mysql.connector 
import os 
from dotenv import load_dotenv

load_dotenv()

class DataBase:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("DB_host"),
            user= os.getenv("BD_USER"),
            password=os.getenv("DB_PASSWORD"),
            datanase=os.getenv("DB_NAME")
        )