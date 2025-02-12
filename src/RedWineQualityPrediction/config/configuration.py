from RedWineQualityPrediction.constanst import *
from RedWineQualityPrediction.entity.config_entity import DataIngstionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig
from RedWineQualityPrediction.utils.common import read_yaml, create_derectories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_derectories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngstionConfig:
        config = self.config.data_ingestion
        
        create_derectories([config.root_dir])
        
        return DataIngstionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
    def data_validation_config(self) -> DataValidationConfig:
        confing = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_derectories([confing.root_dir])
        
        return DataValidationConfig(
            root_dir=confing.root_dir,
            STATUS_FILE=confing.STATUS_FILE,
            unzip_dir=confing.unzip_data_dir,
            all_schema=schema
        )
        
    
    def data_transformation_config(self) -> DataTransformationConfig:
        confing = self.config.data_transformation
        
        create_derectories([confing.root_dir])
        
        return DataTransformationConfig(
            root_dir=confing.root_dir,
            data_path=confing.data_path
        )
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_derectories([config.root_dir])
        
        return ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_derectories([config.root_dir])
        
        return ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            evaluation_metrics_file=config.evaluation_metrics_file,
            target_column=schema.name
        )