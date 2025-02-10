from RedWineQualityPrediction.components.model_trainer import ModelTrainer
from RedWineQualityPrediction.config.configuration import ConfigurationManager
from RedWineQualityPrediction import logger

STAGE_NAME = "Stage 04: Model Trainer"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.training()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error
        