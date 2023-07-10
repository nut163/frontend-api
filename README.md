# API Data Conversion Tool

This tool is an API and a frontend API test website that allows users to convert a variety of data inputs into specified formats. It includes user authentication, usage logging, and billing functionalities.

## Features

1. Data Conversion: Convert data inputs to specified formats.
2. User Authentication: Authenticate users using API keys.
3. Usage Logging: Log usage per user for tracking and billing purposes.
4. Billing: Bill users based on their usage.

## Environment Variables

To setup the environment variables, run the `setup_environment_variables` function in the `infrastructure/setup.py` file. The following environment variables are required:

1. `API_KEY`: The key used for user authentication.
2. `LOG_FILE`: The file where usage logs are stored.
3. `BILLING_INFO`: The information related to user billing.

## Infrastructure Setup and Deployment

To setup and deploy the infrastructure needed to run the application, run the `deploy_application` function in the `infrastructure/deploy.py` file.

## Testing

To test the API, use the `test_api` function in the `frontend/tests/api_tests.js` file.

## Usage

To use the tool, input your data into the `inputField` on the frontend website, select your desired format from the `formatSelect` dropdown, and click the `submitButton`. The converted data will be displayed in the `outputField`.

For any issues or further information, please refer to the individual python and javascript files.