from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define expected columns (same as training)
input_columns = ['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol',
                 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {key: float(request.form[key]) for key in input_columns}
        df = pd.DataFrame([input_data])[input_columns]
        scaled = scaler.transform(df)
        prediction = model.predict(scaled)[0]
        result = "No Disease" if prediction == 0 else "Disease Detected"
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
