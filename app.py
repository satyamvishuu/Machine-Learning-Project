from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import dataIngestionConfig
from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import DataTransformationConfig, DataTranformation
import sys
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = dataIngestionConfig()
        data_ingestion = dataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        #data_transformation_config = dataIngestionConfig()
        data_transformation = DataTranformation()
        train_arr, test_arr,_= data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        model_training = ModelTrainer()
        print(model_training.initiate_model_trainer(train_arr, test_arr))


    except Exception as e:
        logging.info("Custom Exxception")
        raise CustomException(e, sys)