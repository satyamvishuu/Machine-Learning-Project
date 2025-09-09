from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import dataIngestionConfig
from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import DataTransformationConfig, DataTranformation
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = dataIngestionConfig()
        data_ingestion = dataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        #data_transformation_config = dataIngestionConfig()
        data_transformation = DataTranformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)


    except Exception as e:
        logging.info("Custom Exxception")
        raise CustomException(e, sys)