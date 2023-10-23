import os
import sys
import pandas as pd
from src.creditcardDefault import logger
from sklearn.model_selection import train_test_split
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def train_test_split(self):
        try:
            data=pd.read_csv(self.config.data_path)
            
            logger.info("train test split started")
            train,test=train_test_split(data,test_size=0.2)

            train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
            test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

            logger.info("splitted data into train and test datasets")
            logger.info(train.shape)
            logger.info(test.info)

            print(train.shape)
            print(test.shape)
        

        except Exception as e:
            raise CustomException(e,sys)

