import os
import sys
import logging

# define logging format
logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

# define log file path
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_log.log')
# create log directory if not exist
#os.mkdir(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

# configure logging
logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# define logger object
logger = logging.getLogger('RedWineQualityPredictionLogger')