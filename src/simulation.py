import time
import joblib

def simulate_live_detection(X_test):
    model = joblib.load("models/model.pkl")

    print("🚀 Starting Real-Time Threat Detection...\n")

    for i in range(len(X_test)):
        print(i)
        sample = X_test.iloc[i].values.reshape(1, -1)

        prediction = model.predict(sample)

        print(f"🔍 Checking traffic sample {i+1}...")

        if prediction[0] == 1:
            print("🚨 ALERT: Threat Detected!\n")
        else:
            print("✅ Normal Traffic\n")

        time.sleep(1)

    print("✅ Simulation Completed")