from RedWineQualityPrediction import logger
from RedWineQualityPrediction.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline
from RedWineQualityPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from RedWineQualityPrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngetionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error


STAGE_NAME = "Stage 02: Data Validation"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error


STAGE_NAME = "Stage 03: Data Transformation"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
except Exception as error:
    logger.exception(error)
    raise error