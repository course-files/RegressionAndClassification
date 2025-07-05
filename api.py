# Uses Flask, a Python micro web framework, to create a server application:
from flask import Flask, request, jsonify
# Cross-Origin Resource Sharing (CORS)
# Modern browsers apply the "same-origin policy", which blocks web pages from
# making requests to a different origin than the one that served the page.
# This helps prevent malicious sites from reading sensitive data from another
# site you are logged into.
#
# However, there are many legitimate cases where cross-origin requests are
# needed:
#
# Single-page applications (SPA) hosted at example-frontend.com need to call
# APIs hosted at api.example-backend.com.
#
# To support this safely, CORS lets servers explicitly allow such requests.
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Load different models
# It uses joblib to load a trained model, so this API serves ML predictions
decision_tree_model = joblib.load('./model/decisiontree_classifier_baseline.pkl')

# Defines an HTTP endpoint
@app.route('/predict_decision_tree_classifier', methods=['POST'])
def predict_decision_tree():
    # Accepts JSON data sent by a client (browser, curl, Postman, etc.)
    data = request.get_json()
    # Create a DataFrame with the correct feature names
    new_data = pd.DataFrame([{
        'monthly_fee': data.get('monthly_fee'),
        'customer_age': data.get('customer_age'),
        'support_calls': data.get('support_calls')
    }])
    # Performs a prediction using a trained machine learning model)
    prediction = decision_tree_model.predict(new_data)[0]
    # Returns the result as a JSON response:
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

# *1* Sample JSON POST values
# {
#     "monthly_fee": 60,
#     "customer_age": 30,
#     "support_calls": 1
# }

# *2* Sample cURL POST values

# curl -X POST http://127.0.0.1:5000/predict_decision_tree_classifier \
#   -H "Content-Type: application/json" \
#   -d "{\"monthly_fee\": 60, \"customer_age\": 30, \"support_calls\": 1}"

# *3* Sample PowerShell values:

# $body = @{
#     monthly_fee   = 60
#     customer_age  = 30
#     support_calls = 1
# } | ConvertTo-Json
#
# Invoke-RestMethod -Uri http://127.0.0.1:5000/predict_decision_tree_classifier `
#     -Method POST `
#     -Body $body `
#     -ContentType "application/json"