from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load("models/model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([list(data.values())])
    prediction = model.predict(features)

    return jsonify({"Threat": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)