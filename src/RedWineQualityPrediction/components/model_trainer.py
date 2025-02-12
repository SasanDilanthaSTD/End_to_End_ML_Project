import pandas as pd
import os
from RedWineQualityPrediction import logger
from sklearn.linear_model import ElasticNet
from RedWineQualityPrediction.entity.config_entity import ModelTrainerConfig
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def training(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        # target_column = list(self.config.target_column)[0]
        
        train_x = train_data.drop(columns=[self.config.target_column], axis=1)
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
        logger.info(f"Model trained with alpha: {self.config.alpha} and l1_ratio: {self.config.l1_ratio}")
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model saved at: {os.path.join(self.config.root_dir, self.config.model_name)}")