from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import dataIngestionConfig
from src.components.data_ingestion import dataIngestion
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = dataIngestionConfig()
        data_ingestion = dataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exxception")
        raise CustomException(e, sys)