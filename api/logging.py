import os
import logging
from datetime import datetime

LOG_FILE = os.getenv('LOG_FILE')

def log_usage(user_id, data_input, converted_data, format_type):
    logger = logging.getLogger('api_usage')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    log_message = f'User: {user_id}, Input Data: {data_input}, Converted Data: {converted_data}, Format Type: {format_type}'
    logger.info(log_message)