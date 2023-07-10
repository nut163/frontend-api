from flask import Flask, request, jsonify
from .authentication import authenticateUser
from .logging import logUsage
from .billing import calculateBill
from .utils import convertData
from .models import DataInput

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def convert():
    user = authenticateUser(request.headers.get('Authorization'))
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401

    data_input = DataInput(**request.json)
    converted_data = convertData(data_input)

    logUsage(user)
    bill = calculateBill(user)

    return jsonify({
        'convertedData': converted_data,
        'bill': bill
    }), 200

if __name__ == "__main__":
    app.run(debug=True)