import os
import sys
import logging

log_str = "[%(asctime)s - %(levelname)s - %(module)s] - %(message)s"

log_dir = "logs"
LOG_FILE_PATH = os.path.join(log_dir, "Running.logs")

os.makedirs(log_dir, exist_ok= True)


logging.basicConfig(
    format= log_str,
    level= logging.INFO,
    handlers= [
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("predictive_maintenance")
