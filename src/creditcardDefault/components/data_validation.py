import os
import sys
import pandas as pd
from creditcardDefault.exception import CustomException
from creditcardDefault.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_data(self)->bool:
        try:
            validation_status=None

            df=pd.read_csv(self.config.unzip_dir)
            all_cols=list(df.columns)

            all_schema=self.config.all_schema.keys()

            for cols in all_cols:
                if cols not in all_schema:
                    validation_status=False
                    with open(self.config.status_file,"w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.status_file,"w") as f:
                        f.write(f"Validation status: {validation_status}")
                
                return validation_status
        except Exception as e:
            raise CustomException(e,sys)


