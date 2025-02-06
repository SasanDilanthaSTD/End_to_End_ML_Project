import os
from RedWineQualityPrediction import logger
import pandas as pd
from RedWineQualityPrediction.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            
            dataset = pd.read_csv(self.config.unzip_dir)
            all_cols = list(dataset.columns)
            
            all_schemas = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schemas:
                    validation_status=False
                    logger.info(f"ERRO: {col} is not in schema")
                else:
                    validation_status=True
            if validation_status:
                # Validate the columns datatypes
                    expected_schema = self.config.all_schema # get key and value both pares
                    
                    for col, expec_dtype in expected_schema.items():
                        dataset_col_dtype = dataset[col].dtype
                        
                        # compare the csv file data type and schema data type
                        if dataset_col_dtype != expec_dtype :
                            validation_status=False
                            logger.info(f"ERRO: {col} data type is {dataset_col_dtype} and schema data type is {expec_dtype}")
                        else:
                            validation_status=True
                            logger.info(f"Data validation success in :: {col}")
                    
            with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}")
                        
            return validation_status
            
        except Exception as error:
            raise error
 