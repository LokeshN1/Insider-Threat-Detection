# Insider Threat Detection - Backend

## Overview

The backend of the Insider Threat Detection project is built using Flask, a lightweight WSGI web application framework in Python. This application is designed to detect anomalies in user behavior data through machine learning models, specifically using the Isolation Forest algorithm.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Details](#model-details)
- [Contributing](#contributing)


## Features

- Predicts anomalies in user behavior data.
- Uses pre-trained models for real-time anomaly detection.
- Scalable architecture to accommodate future enhancements.
- CORS enabled for cross-origin requests.


## Installation

To run the backend application, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Insider-Threat-Detection.git
   cd Insider-Threat-Detection/backend


### Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Ensure you have `Flask`, `Flask-CORS`, `pandas`, `numpy`, `scikit-learn`, and `joblib` in your `requirements.txt`.

## Usage

To start the Flask application, run:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/predict`.

## API Endpoints

### POST /predict

**Description**: This endpoint receives user behavior data and returns anomaly predictions.

**Request Body**: JSON format with the following fields:

```json
[
    {
        "email_count": 3683,                 // int64
        "unique_to": 1558,                   // int64
        "unique_cc": 399,                    // int64
        "unique_bcc": 0,                     // int64
        "unique_from": 2,                    // int64
        "avg_size": 29967.796362,            // float64
        "max_size": 86390,                   // int64
        "total_attachments": 0,               // int64
        "logon_count": 5,                    // Example value (int64)
        "device_connect_count": 1.5,         // Example value (float64)
        "file_transfer_count": 2.0,          // Example value (float64)
        "avg_content_length": 250.0,         // Example value (float64)
        "O": 42,                              // int64
        "C": 44,                              // int64
        "E": 32,                              // int64
        "A": 30,                              // int64
        "N": 26,                              // int64
        "first_logon_seconds": 1294045020,  // Example float64 (time in seconds)
        "last_logon_seconds": 1294044520    // Example float64 (time in seconds)
    }
]

```

**Response**: Returns a JSON object with predictions and anomaly scores.


## Model Details

The application utilizes a pre-trained Isolation Forest model and a Standard Scaler for preprocessing input data. These models are loaded at startup, and predictions are made based on incoming data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.
