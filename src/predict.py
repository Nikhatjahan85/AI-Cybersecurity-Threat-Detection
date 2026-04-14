import joblib

def load_model():
    return joblib.load("models/model.pkl")

def predict(model, data):
    return model.predict(data)