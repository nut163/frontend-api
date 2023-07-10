import unittest
from main import app
from models import User, DataInput
from authentication import authenticateUser
from utils import convertData
from logging import logUsage
from billing import calculateBill

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_api(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_authenticateUser(self):
        user = User('testuser', 'testpassword')
        self.assertTrue(authenticateUser(user))

    def test_convertData(self):
        data_input = DataInput('test data')
        self.assertEqual(convertData(data_input), 'converted data')

    def test_logUsage(self):
        user = User('testuser', 'testpassword')
        logUsage(user)
        self.assertEqual(user.usage, 1)

    def test_calculateBill(self):
        user = User('testuser', 'testpassword')
        user.usage = 5
        self.assertEqual(calculateBill(user), 50)

if __name__ == "__main__":
    unittest.main()