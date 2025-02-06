import os
from RedWineQualityPrediction import logger
import pandas as pd
from sklearn.model_selection import train_test_split


from RedWineQualityPrediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_spliting(self):
        dataset = pd.read_csv(self.config.data_path)
        
        # spliting the data set into traingin and testing. 75% 25%
        train, test = train_test_split(dataset)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False)
        
        logger.info("Splied data into traing and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)