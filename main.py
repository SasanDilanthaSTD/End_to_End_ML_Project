from RedWineQualityPrediction import logger
from RedWineQualityPrediction.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline


STAGE_NAME = "Stage 01: Data Ingestion"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngetionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error