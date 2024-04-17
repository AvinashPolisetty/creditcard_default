import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.creditcardDefault.exception import CustomException
from src.creditcardDefault import logging

from src.creditcardDefault.utils.common import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl") 

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestClassifier(),
                
            }
            params={
                
                "Random Forest":{
                    'criterion':['gini', 'entropy'],
                    'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32],
                    'bootstrap':[True]
                },
                
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models, parameter=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found",sys)
            
            logging.info(f"Best Model found on both training and testing dataset > {best_model}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            model_accuracy_score = accuracy_score(y_test, predicted)

            model_confusion_matrix = confusion_matrix(y_test, predicted)

            return ( model_accuracy_score,
                    model_confusion_matrix)
            



            
        except Exception as e:
            raise CustomException(e,sys)