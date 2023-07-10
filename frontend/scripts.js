const API_KEY = 'YOUR_API_KEY_HERE'; // Replace with your API key
const API_URL = 'http://localhost:5000'; // Replace with your API URL

const inputField = document.getElementById('inputField');
const outputField = document.getElementById('outputField');
const formatSelect = document.getElementById('formatSelect');
const submitButton = document.getElementById('submitButton');

submitButton.addEventListener('click', async () => {
    const data_input = inputField.value;
    const format_type = formatSelect.value;

    const response = await fetch(`${API_URL}/convert`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${API_KEY}`
        },
        body: JSON.stringify({ data_input, format_type })
    });

    if (response.ok) {
        const { converted_data } = await response.json();
        outputField.value = converted_data;
    } else {
        outputField.value = 'Error: Unable to convert data';
    }
});

async function test_api() {
    const test_data = 'Test data';
    const test_format = 'Test format';

    const response = await fetch(`${API_URL}/convert`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${API_KEY}`
        },
        body: JSON.stringify({ data_input: test_data, format_type: test_format })
    });

    if (response.ok) {
        console.log('API Test Passed');
    } else {
        console.log('API Test Failed');
    }
}

test_api();