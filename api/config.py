import os

class Config:
    API_KEY = os.getenv('API_KEY')
    LOG_FILE = os.getenv('LOG_FILE')
    BILLING_INFO = os.getenv('BILLING_INFO')