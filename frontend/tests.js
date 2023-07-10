```javascript
// Import necessary modules
import { testAPI } from '../api/tests.py';

// Define DOM elements
const inputField = document.getElementById('inputField');
const submitButton = document.getElementById('submitButton');
const successMessage = document.getElementById('successMessage');
const errorMessage = document.getElementById('errorMessage');

// Define test function
function runTests() {
    // Test 1: Check if API can handle data input and conversion
    let dataInput = 'Test data';
    let expectedOutput = 'Converted data';
    testAPI(dataInput, expectedOutput, 'Data Conversion Test');

    // Test 2: Check if API can handle user authentication
    let username = 'TestUser';
    let password = 'TestPassword';
    testAPI(username, password, 'User Authentication Test');

    // Test 3: Check if API can log usage correctly
    let usageData = 'Test usage data';
    testAPI(usageData, 'Usage Logging Test');

    // Test 4: Check if API can calculate bill correctly
    let billData = 'Test bill data';
    testAPI(billData, 'Billing Test');
}

// Event listener for submit button
submitButton.addEventListener('click', () => {
    // Clear messages
    successMessage.textContent = '';
    errorMessage.textContent = '';

    // Run tests
    try {
        runTests();
        successMessage.textContent = 'All tests passed successfully!';
    } catch (error) {
        errorMessage.textContent = 'Some tests failed. Check console for details.';
        console.error(error);
    }
});
```