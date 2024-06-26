import os
import sys
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass




@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")
   


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered into the data ingestion method")
        try:
            path = r'research\UCI_Credit_Card.csv'
            df = pd.read_csv(path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info('Make a directory for training data')

            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            logging.info('Save that dataframe into a csv file name as [data.csv] into the artifacts directory')

            logging.info('Train Test Split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info('Save the train data as a csv file into artifacts folder')

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Save the test data as csv file into artifacts folder')
        
            logging.info('Ingestion of the data has been completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        

