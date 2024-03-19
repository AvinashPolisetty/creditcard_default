import pandas as pd
import os
from src.exception import CustomException
from src.logger import logging
import joblib
import sys
from creditcardDefault.entity import ModelTrainingConfig

from sklearn.ensemble import RandomForestClassifier


class ModelTraining:
    def __init__(self,config:ModelTrainingConfig):
        self.config=config


    try:

        def training(self):
            train_data=pd.read_csv(self.config.train_data_path)
            test_data=pd.read_csv(self.config.test_data_path)

            X_train = train_data.drop([self.config.target_name],axis=1)
            X_test = test_data.drop([self.config.target_name],axis=1)

            y_train=train_data[[self.config.target_column]]
            y_test=test_data[[self.config.target_column]]

            rf=RandomForestClassifier(n_estimators=self.config.n_estimators,criterion=self.config.criterion,max_depth=self.config.max_depth,min_samples_split=self.config.min_samples_split)
            rf.fit(X_train,y_train)

            joblib.dump(rf,os.path.join(self.config.root_dir,self.config.model_name))
    except Exception as e:
        raise CustomException(e,sys)




    
