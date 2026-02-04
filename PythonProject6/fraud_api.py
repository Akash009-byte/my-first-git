from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# 1. Load the model we trained in fraud_detection.py
# Make sure fraud_model.pkl is in your project folder!
model = joblib.load('fraud_model.pkl')


# 2. This route "induces" the visual page when you visit http://127.0.0.1:5001
@app.route('/')
def home():
    return render_template('fraud_index.html')


# 3. This route handles the actual math/prediction
@app.route('/check_transaction', methods=['POST'])
def check_transaction():
    # Check if data is coming from the HTML form or a JSON test script
    if request.form.get('features'):
        # Data from Browser: "500, 1.2, 0.5, 10, 100" -> [500.0, 1.2, ...]
        raw_data = request.form.get('features').split(',')
        features = [float(i) for i in raw_data]
    else:
        # Data from test_fraud.py
        data = request.get_json()
        features = data['features']

    # Format the data for the model
    input_features = np.array(features).reshape(1, -1)

    # Make the prediction (0 = Legit, 1 = Fraud)
    prediction = model.predict(input_features)
    result = "Fraudulent" if prediction[0] == 1 else "Legitimate"

    return f"""
    <h1>Analysis Result</h1>
    <p>The system has classified this transaction as: <strong>{result}</strong></p>
    <a href='/'>Check another transaction</a>
    """


if __name__ == '__main__':
    # Running on port 5001 so it doesn't clash with the Resume Ranker
    app.run(port=5001, debug=True)