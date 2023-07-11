import os
from flask import Flask
from api.app import app

def deploy_application():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    deploy_application()