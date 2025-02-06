from RedWineQualityPrediction.components.data_validation import DataValidation
from RedWineQualityPrediction.config.configuration import ConfigurationManager
from RedWineQualityPrediction import logger

STAGE_NAME = "Stage 02: Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_val_config = config.data_validation_config()
        data_val = DataValidation(config=data_val_config)
        data_val.validate_all_columns()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error