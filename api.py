from flask import Flask, request, jsonify
# CORS (Cross-Origin Resource Sharing)
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Load different models
decision_tree_model = joblib.load('./model/decisiontree_classifier_baseline.pkl')

@app.route('/predict_decision_tree', methods=['POST'])
def predict_decision_tree():
    data = request.get_json()
    # Create a DataFrame with the correct feature names
    X = pd.DataFrame([{
        'monthly_fee': data.get('monthly_fee'),
        'customer_age': data.get('customer_age'),
        'support_calls': data.get('support_calls')
    }])
    prediction = decision_tree_model.predict(X)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

# Sample JSON POST values
# {
#     "monthly_fee": 60,
#     "customer_age": 30,
#     "support_calls": 1
# }

# Sample cURL POST values
# curl -X POST http://127.0.0.1:5000/predict_decision_tree \
#   -H "Content-Type: application/json" \
#   -d "{\"monthly_fee\": 60, \"customer_age\": 30, \"support_calls\": 1}"