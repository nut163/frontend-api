const axios = require('axios');

const API_KEY = process.env.API_KEY;
const test_api = async () => {
    const user_id = 'test_user';
    const data_input = 'test_data';
    const format_type = 'json';

    try {
        const response = await axios.post('http://localhost:5000/convert', {
            user_id,
            API_KEY,
            data_input,
            format_type
        });

        if (response.data.converted_data) {
            console.log('Data conversion test passed');
        } else {
            console.log('Data conversion test failed');
        }
    } catch (error) {
        console.error(`Error in API test: ${error}`);
    }
};

test_api();