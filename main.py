from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
import sys

Stage_name="Data Ingestion"

try:
    logger.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)

    
    
