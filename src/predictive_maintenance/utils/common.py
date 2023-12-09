from src.predictive_maintenance import logger
from exception import CustomException
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import sys

load_dotenv()
uri = os.getenv("uri")

def connect_to_database():
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client["use predictive_maintenance"]
        logger.info("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        logger.info(CustomException(e,sys))
        raise CustomException(e,sys)
        
