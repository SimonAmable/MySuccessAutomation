import logging
import os
from datetime import datetime

LOG_DIR = 'log'
os.makedirs(LOG_DIR, exist_ok=True)

# Define the log file name with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
log_file_name = "app_" + timestamp + ".log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, log_file_name)),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def log_info(msg):
    logger.info(msg)
    
def log_error(msg):
    logger.error(msg)

def log_success(msg):
    logger.info(msg)

# Override the print function with the logger because i'm lazy and wanna finish this projectif since i cant even use it lol
def print(msg):
    logger.info(msg)