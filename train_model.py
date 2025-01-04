import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load training data
data = pd.read_csv("training_data.csv")

# Features and Labels
X = data[["current"]]
y = data["theft"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save the model
with open("theft_detection_model.pkl", "wb") as f:
    pickle.dump(model, f)
