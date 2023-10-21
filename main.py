from src.creditcardDefault import logger
from src.creditcardDefault.exception import CustomException
import sys

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:

        logger.info("Divided by 0")
        raise CustomException(e,sys)