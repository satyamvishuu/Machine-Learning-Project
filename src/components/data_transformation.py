import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_obj



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('data','preprocessor.pkl')

class DataTranformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_tranformation_obj(self):
        '''
        this function is responsible for data transformation
        '''    
        try:
            num_columns = ["writing score", "reading score"]
            cat_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course"
            ]
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ("scaler",StandardScaler())
            ])
            
            cat_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='most_frequent')),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical Columns: {cat_columns}")
            logging.info(f"Numerical Columns: {num_columns}")

            preprocessor= ColumnTransformer([
                ("num_pipeline", num_pipeline, num_columns),
                ("cat_pipeline", cat_pipeline, cat_columns)
            ])

            return preprocessor
        


            pass
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Reading train and test file")

            preprocessing_obj=self.get_data_tranformation_obj()

            target_column_name = "math score"
            num_columns = ["writing score", "reading score"]

            # divide the train dataset to independent and dependent feature

            input_features_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_features_train_df = train_df[target_column_name]

            # divide the test dataset to independent and dependent feature

            input_features_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_features_test_df = test_df[target_column_name]

            logging.info("Applying preprocssing on training and test dataframe")

            input_features_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr=preprocessing_obj.transform(input_features_test_df)


            train_arr = np.c_[
                input_features_train_arr, np.array(target_features_train_df)
            ]
            test_arr = np.c_[
                input_features_test_arr, np.array(target_features_test_df)
            ]

            logging.info(f"Saved preprocessing Object")

            save_obj(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

            
        except Exception as e:
            raise CustomException(e,sys)