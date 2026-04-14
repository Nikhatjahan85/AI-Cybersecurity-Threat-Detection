# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Import your modules
from src.preprocessing import load_data, preprocess
from src.model import train_model, save_model
from src.visualize import plot_confusion
from src.simulation import simulate_live_detection

# Load dataset
data = load_data("data/dataset.csv")
print(list(data.columns))
# Preprocess data
X, y = preprocess(data)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = train_model(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n📊 Model Performance:\n")
print(classification_report(y_test, y_pred))

# Plot confusion matrix
plot_confusion(y_test, y_pred)

# Save model
save_model(model)

# Run real-time simulation
simulate_live_detection(X_test)
from src.simulation import simulate_live_detection

simulate_live_detection(X_test)
