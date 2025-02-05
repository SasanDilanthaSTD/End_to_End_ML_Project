from RedWineQualityPrediction.components.data_ingestion import DataIngestion
from RedWineQualityPrediction.config.configuration import ConfigurationManager
from RedWineQualityPrediction import logger

STAGE_NAME = "Stage 01: Data Ingestion"

class DataIngetionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingetion = DataIngestion(config=data_ingestion_config)
        data_ingetion.download_data_file()
        data_ingetion.unzip_data_file()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = DataIngetionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error