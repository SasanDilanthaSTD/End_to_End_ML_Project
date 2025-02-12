from RedWineQualityPrediction.components.model_evaluation import ModelEvaluation
from RedWineQualityPrediction.config.configuration import ConfigurationManager
from RedWineQualityPrediction import logger

STAGE_NAME = "Stage 05: Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        cofig = ConfigurationManager()
        model_eval_mgr = cofig.get_model_evaluation_config()
        model_eval = ModelEvaluation(model_eval_mgr)
        model_eval.save_results()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
    except Exception as error:
        logger.exception(error)
        raise error
        