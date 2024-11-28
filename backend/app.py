from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os  # Import os to access environment variables

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load pre-trained model and scaler
model = joblib.load("isolation_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data
        input_data = request.json
        
        # Convert input data to a DataFrame
        input_df = pd.DataFrame(input_data)
        
        # Scale the input data
        input_scaled = scaler.transform(input_df)
        
        # Predict using Isolation Forest
        predictions = model.predict(input_scaled)
        anomaly_scores = model.decision_function(input_scaled)

        # Convert predictions to human-readable format
        results = {
            "predictions": ["Anomaly" if pred == -1 else "Normal" for pred in predictions],
            "anomaly_scores": anomaly_scores.tolist()
        }

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Get the PORT environment variable (default to 5000 for local testing)
    port = int(os.environ.get("PORT", 5000))
    # Bind to all interfaces and use the correct port
    app.run(host='0.0.0.0', port=port)
