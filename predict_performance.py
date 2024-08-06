from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('performance_model.joblib')

# Define the mapping from integers to labels
LABEL_MAP = {
    0: 'Distinction',
    1: 'Upper Credit',
    2: 'Lower Credit'
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    study_hours = data['studyHours']
    punctuality = data['punctuality']
    gpa1 = data['gpa1']
    gpa2 = data['gpa2']
    gpa3 = data['gpa3']

    # Prepare the data for prediction
    input_data = np.array([[study_hours, punctuality, gpa1, gpa2, gpa3]])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_label = LABEL_MAP.get(prediction[0], 'Unknown')

    return jsonify({'prediction': prediction_label})

if __name__ == '__main__':
    app.run(debug=True)
