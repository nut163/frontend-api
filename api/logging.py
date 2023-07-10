import logging
from models import User

def logUsage(user: User, usage_data):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('usage.log')
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    log_message = f"User: {user.username}, Usage: {usage_data}"
    logger.info(log_message)