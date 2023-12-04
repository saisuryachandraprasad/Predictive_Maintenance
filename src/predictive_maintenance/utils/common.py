from src.predictive_maintenance import logger
from exception import CustomException
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import sys

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")

def connect_database():
    """connect to data base"""

    try:
        logger.info("Connecting to database")
        MongoClient("mongodb+srv://user:password@predictivemaintenance.nyvwsjt.mongodb.net/?retryWrites=true&w=majority")
        
        logger.info("connection established with database")

    except Exception as e:
        logger.info(CustomException(e,sys))
        raise CustomException(e,sys)
