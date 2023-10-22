from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.components.data_ingestion import DataIngestion
from src.creditcardDefault.exception import CustomException
import sys

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_file()
        except Exception as e:
            raise CustomException(e,sys)