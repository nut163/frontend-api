import os

def setup_environment_variables():
    os.environ['API_KEY'] = 'your-api-key'
    os.environ['LOG_FILE'] = '/path/to/your/log/file'
    os.environ['BILLING_INFO'] = '/path/to/your/billing/info/file'

if __name__ == "__main__":
    setup_environment_variables()