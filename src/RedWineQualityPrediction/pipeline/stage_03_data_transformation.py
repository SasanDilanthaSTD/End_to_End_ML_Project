from RedWineQualityPrediction.components.data_transformation import DataTransformation
from RedWineQualityPrediction.config.configuration import ConfigurationManager
from RedWineQualityPrediction import logger

STAGE_NAME = "Stage 03: Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
                
            if status == "True":
                config = ConfigurationManager()
                data_trm_config = config.data_transformation_config()
                data_trm = DataTransformation(config=data_trm_config)
                data_trm.train_test_spliting()
            else:
                raise Exception("You data schema is not valied")
        except Exception as error:
            print(error)
        