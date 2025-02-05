import os
import urllib.request as request
import zipfile
from RedWineQualityPrediction import logger
from RedWineQualityPrediction.entity.config_entity import DataIngstionConfig
from RedWineQualityPrediction.utils.common import get_size
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngstionConfig):
        self.config = config
        
    def download_data_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {file_name} with folowing infor: \n {headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file} and size of the file is: {get_size(Path(self.config.local_data_file))}")
    
    
    def unzip_data_file(self):
        """
        zip_file_path: str
        extract the zip file in to the data directory
        Function return none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)