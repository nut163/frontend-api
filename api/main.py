from flask import Flask, request
from .routes import api_routes
from .models import User, DataInput
from .utils import convertData
from .authentication import authenticateUser
from .logging import logUsage
from .billing import calculateBill

app = Flask(__name__)
app.register_blueprint(api_routes)

@app.route('/api/data', methods=['POST'])
def handle_data():
    user = authenticateUser(request.headers.get('Authorization'))
    if not user:
        return {'message': 'Unauthorized'}, 401

    data_input = DataInput(request.json)
    if not data_input.is_valid():
        return {'message': 'Invalid data input'}, 400

    converted_data = convertData(data_input)
    logUsage(user, data_input)
    bill = calculateBill(user)

    return {'convertedData': converted_data, 'bill': bill}, 200

if __name__ == '__main__':
    app.run(debug=True)