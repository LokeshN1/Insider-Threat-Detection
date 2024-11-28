const form = document.getElementById('dataForm');
const output = document.getElementById('output');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const inputData = document.getElementById('inputData').value;

    try {
        // Parse input data as JSON
        const jsonData = JSON.parse(inputData);

        // Send data to backend API
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jsonData),
        });

        // Handle response
        const result = await response.json();
        if (response.ok) {
            output.innerHTML = `
                <p><strong>Predictions:</strong> ${result.predictions.join(", ")}</p>
                <p><strong>Anomaly Scores:</strong> ${result.anomaly_scores.join(", ")}</p>
            `;
        } else {
            output.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
        }
    } catch (error) {
        output.innerHTML = `<p style="color: red;">Invalid input data or server error.</p>`;
    }
});
