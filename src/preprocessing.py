import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(path):
    return pd.read_csv(path)

def preprocess(data):
    data = data.dropna()

    if "Timestamp" in data.columns:
        data = data.drop("Timestamp", axis=1)

    X = data.drop("label", axis=1)
    y = data["label"]
def preprocess(data):
    data = data.dropna()

    if 'Timestamp' in data.columns:
        data = data.drop('Timestamp', axis=1)

    target_column = data.columns[-1]

    X = data.drop(target_column, axis=1)
    y = data[target_column]

    return X, y
