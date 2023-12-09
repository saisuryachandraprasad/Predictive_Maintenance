from src.predictive_maintenance import logger
from exception import CustomException
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import pandas as pd
import os
import sys

load_dotenv()
uri=os.getenv("uri")

def reading_data_from_database():
        try:
            logger.info("Reading data from database is strated")
            client = MongoClient(uri)
            database = client['PredictiveMaintenance']
            collection = database['PredictiveMaintenance']
            data = collection.find({})
            df = pd.DataFrame(data)
            logger.info("Complted reading data from database")

            return df      
        except Exception as e:
              logger.info(CustomException(e,sys))
              raise CustomException(e,sys)