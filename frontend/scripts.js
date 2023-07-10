const inputField = document.getElementById('inputField');
const submitButton = document.getElementById('submitButton');
const successMessage = document.getElementById('successMessage');
const errorMessage = document.getElementById('errorMessage');

submitButton.addEventListener('click', async () => {
    const inputData = inputField.value;
    const response = await fetch('/api/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: inputData })
    });

    if (response.ok) {
        const result = await response.json();
        successMessage.textContent = `Conversion successful: ${result.data}`;
        errorMessage.textContent = '';
    } else {
        const error = await response.json();
        errorMessage.textContent = `Error: ${error.message}`;
        successMessage.textContent = '';
    }
});