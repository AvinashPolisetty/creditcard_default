from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.components.model_training import ModelTraining
from src.creditcardDefault.exception import CustomException
import sys


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass


    def main(self):

        try:
            config = ConfigurationManager()
            model_train_config=config.get_data_model_train()
            model_train_config=ModelTraining(config=model_train_config)
            model_train_config.training()

        except Exception as e:
            raise CustomException(e,sys)