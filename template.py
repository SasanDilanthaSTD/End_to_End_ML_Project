import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Set Project Name
project_name = 'RedWineQualityPrediction'

# Set Project Directory
list_of_dirs = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constanst/__init__.py",
    "config/config.yml",
    "params.yml",
    "schema.yml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# logic for create folders and files
for dir in list_of_dirs:
    filepath = Path(dir)
    file_dir, file_name = os.path.split(filepath) # seperate file name and directory
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory: {file_dir} for file: {file_name}")
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Creating Empty File: {file_name} in Directory: {file_dir}")
    else:
        logging.info(f"File: {file_name} already exists in Directory: {file_dir}")
        