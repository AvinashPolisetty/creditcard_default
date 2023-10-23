from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.components.data_transformation import DataTransformation
from src.creditcardDefault.exception import CustomException
import sys
from pathlib import Path

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"),'r') as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transform_config=config.get_data_transformation_config()
                data_transform=DataTransformation(config=data_transform_config)
                data_transform.train_test_split()

            else:
                raise Exception("data schema is not valid")
        except Exception as e:
            raise CustomException(e,sys)


