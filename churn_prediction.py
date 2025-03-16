# churn_prediction_updated.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify
import pickle
import os

# Simulated dataset creation (replace with real data in production)
def create_sample_data():
    np.random.seed(42)
    data = {
        'usage_freq': np.random.randint(1, 100, 1000),  # Usage frequency (1-100)
        'payment_delay': np.random.randint(0, 30, 1000),  # Days late on payment
        'support_tickets': np.random.randint(0, 10, 1000),  # Support tickets opened
        'churn': np.random.choice([0, 1], 1000, p=[0.8, 0.2])  # 20% churn rate
    }
    return pd.DataFrame(data)

# Train and save the model
def train_model():
    df = create_sample_data()
    X = df[['usage_freq', 'payment_delay', 'support_tickets']]
    y = df['churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    
    # Save model
    with open('churn_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return model

# Load model
def load_model():
    if not os.path.exists('churn_model.pkl'):
        return train_model()
    with open('churn_model.pkl', 'rb') as f:
        return pickle.load(f)

# Flask API
app = Flask(__name__)
model = load_model()

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the Churn Prediction API!',
        'endpoints': {
            '/health': 'GET - Check API status',
            '/predict': 'POST - Predict churn (send JSON: {"usage_freq": int, "payment_delay": int, "support_tickets": int})'
        }
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            data['usage_freq'],
            data['payment_delay'],
            data['support_tickets']
        ]
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1]
        return jsonify({
            'churn_prediction': int(prediction),
            'churn_probability': float(probability)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    if not os.path.exists('churn_model.pkl'):
        train_model()
    app.run(host='0.0.0.0', port=5000, debug=False)