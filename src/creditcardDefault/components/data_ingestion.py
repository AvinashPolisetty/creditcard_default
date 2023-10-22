import os
import sys
import zipfile
import urllib.request as request
from pathlib import Path
from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException
from src.creditcardDefault.utils.common import get_size
from src.creditcardDefault.config.configuration import ConfigurationManager
from src.creditcardDefault.entity import DataIngestionConfig


class DataIngestion:
    try:
        def __init__(self,config:DataIngestionConfig):
            self.config=config

        def download_file(self):
            if not os.path.exists(self.config.local_data_file):
                filename,headers=request.urlretrieve(url=self.config.source_url,filename=self.config.local_data_file)
                logger.info(f"{filename} download! with following info in headers")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


        def extract_file(self):
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                
    except Exception as e:
        raise CustomException(e,sys)