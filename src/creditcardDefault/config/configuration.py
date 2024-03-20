from src.creditcardDefault.constants import *
from src.creditcardDefault.entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,
                                                    ModelTrainingConfig,ModelEvaluationConfig)
from src.creditcardDefault.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self,
                config_filepath=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH,
                schema_filepath=SCHEMA_FILE_PATH):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.columns

        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            status_file=config.status_file,
            all_schema=schema,

        )

        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )


        return data_transformation_config


    def get_data_model_train(self)->ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.RandomForestClassifier
        schema = self.schema.target

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name = config.model_name,
            target_column = schema.name,
            n_estimators= params.n_estimators,
            criterion = params.criterion,
            max_depth= params.max_depth,
            min_samples_split=params.min_samples_split


        )

        return model_training_config
    

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config= self.config.model_evaluation
        params= self.params.RandomForestClassifier
        schema = self.schema.target

        create_directories([config.root_dir])

        model_eval_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metrics_file_path=config.metrics_file_path,
            all_params=params,
            target_column=schema.name
        )

        return model_eval_config




        
