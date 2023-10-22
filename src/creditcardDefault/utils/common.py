import os
import sys
import yaml
from pathlib import Path
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox
from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logger.info(f"created directory:{path}")
    except Exception as e:
        raise CustomException(e,sys)
    
    
@ensure_annotations
def get_size(path:Path): 
    size=round(os.path.getsize(path)/1024)
    return  f"~ {size} KB"
