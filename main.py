from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.creditcardDefault.pipeline.stage02_data_validation import DataValidationPipeline
from src.creditcardDefault.pipeline.stage03_data_transformation import DataTransformationPipeline
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
   
   
    
