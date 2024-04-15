from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException

import sys

Stage_name="Data Ingestion"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)

    
Stage_name="Data Validation"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_validation=DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)


Stage_name="Data Transformation"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_transform=DataTransformationPipeline()
    data_transform.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)
   
   


Stage_name="Model Training"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_transform=ModelTrainingPipeline()
    data_transform.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)
   
    

Stage_name="Model Evaluation"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_transform=ModelEvaluationPipeline()
    data_transform.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)
   
