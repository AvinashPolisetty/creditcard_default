from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.components.data_validation import DataValidation
from src.creditcardDefault.exception import CustomException
import sys

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_validation_config=config.get_data_validation_config()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_data()
        except Exception as e:
            raise CustomException(e,sys)