import os
from box.exceptions import BoxValueError
import yaml
from RedWineQualityPrediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read the yaml files and return
    
    ARGS:
        path_to_yaml(str): Path: Path to yaml file
    
    RAISES:
        BoxValueError: If the yaml file is emty
        e: emty yaml file
        
    RETURNS:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from ::     {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_derectories(path_to_derectories: list, verbose=True):
    """create list of derectories
    
    ARGS:
        path_to_derectories(list): List of derectories
        verbose(bool): Print the message
    """
    
    for dir in path_to_derectories:
        os.makedirs(dir, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at :: {dir}")
   
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save the data in json format
    
    ARGS:
        path(str): Path to save the json file
        data(dict): Data to save in json format
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    logger.info(f"Data saved in json format at :: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load the json file
    
    ARGS:
        path(str): Path to json file
        
    RETURNS:
        ConfigBox: ConfigBox object
    """
    with open(path) as json_file:
        data = json.load(json_file)
        
    logger.info(f"Data loaded from json file at :: {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save the data in binary format
    
    ARGS:
        data(Any): Data to save in binary format
        path(str): Path to save the binary file
    """
    joblib.dump(data, path)
    logger.info(f"Data saved in binary format at :: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load the binary file
    
    ARGS:
        path(str): Path to binary file
        
    RETURNS:
        Any: Data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from binary file at :: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of the file in KB
    
    ARGS:
        path(str): Path to file
        
    RETURNS:
        str: Size of the file
    """
    size = round(os.path.getsize(path)/1024, 2)
    return f"~{size} KB"