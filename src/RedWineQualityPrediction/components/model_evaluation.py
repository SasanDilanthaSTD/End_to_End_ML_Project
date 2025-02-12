from pathlib import Path
import pandas as pd
from RedWineQualityPrediction import logger
from sklearn.linear_model import ElasticNet
from RedWineQualityPrediction.entity.config_entity import ModelEvaluationConfig
from RedWineQualityPrediction.utils.common import save_json
import joblib
from urllib.parse import urlparse
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, predict):
        rmse = np.sqrt(mean_squared_error(actual, predict))
        mae = mean_absolute_error(actual, predict)
        r2 = r2_score(actual, predict)
        return rmse, mae, r2
    
    
    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)
        
        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
        
        # save metrics
        scores = {"RMSE": rmse, "MAE": mae, "R2": r2}
        save_json(path=Path(self.config.evaluation_metrics_file), data=scores)