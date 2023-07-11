from flask import Flask, request, jsonify
import os
from authentication import authenticate_user
from data_conversion import convert_data
from logging import log_usage
from billing import bill_user

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    user_id = data.get('user_id')
    data_input = data.get('data_input')
    format_type = data.get('format_type')

    if not authenticate_user(user_id, API_KEY):
        return jsonify({"error": "Invalid API Key"}), 401

    try:
        converted_data = convert_data(data_input, format_type)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    log_usage(user_id, data_input, format_type)
    bill_user(user_id)

    return jsonify({"converted_data": converted_data}), 200

if __name__ == '__main__':
    app.run(debug=True)