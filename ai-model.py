from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Load data
data = pd.read_csv("electricity_data.csv")

# Features (Voltage, Current) and target (TheftFlag)
X = data[['Voltage', 'Current']]
y = data['TheftFlag']

# Split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Save the model to a file
joblib.dump(model, "theft_detection_model.pkl")
print("Model saved as theft_detection_model.pkl")
