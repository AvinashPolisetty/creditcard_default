import sys
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault import logging
from src.creditcardDefault.components.data_transformation import DataTransformation

from src.creditcardDefault.components.data_ingestion import DataIngestion



def training_pipeline():
    try:
        
        obj = DataIngestion()
        logging.info('Data Ingestion has started')
        train_data, test_data = obj.initiate_data_ingestion()
        logging.info('Get the train and test data')

        data_transformation = DataTransformation()
        logging.info('Data transformation has started')
        data_transformation.initiate_data_transformation(train_data, test_data)
        logging.info('Get the train and test array for model building')

       

    except Exception as e:
            raise CustomException(e, sys)
    

if __name__ == "__main__":
     training_pipeline()