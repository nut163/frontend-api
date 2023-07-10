import os
from flask import request, jsonify

API_KEY = os.getenv("API_KEY")

def authenticate_user():
    if 'Authorization' not in request.headers:
        return jsonify({"message": "Missing authorization header"}), 401

    auth_header = request.headers['Authorization']
    token = auth_header.split(" ")[1]

    if not token or token != API_KEY:
        return jsonify({"message": "Invalid API key"}), 403

    return None