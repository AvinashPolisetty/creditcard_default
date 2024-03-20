from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_metrics()
        except Exception as e:
            raise e