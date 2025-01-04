import pandas as pd
import joblib

# Load the trained model
model = joblib.load("theft_detection_model.pkl")

# Simulate new data with feature names (Voltage, Current)
new_data = pd.DataFrame(
    [[220, 15], [210, 5], [230, 25]],  # Example inputs
    columns=["Voltage", "Current"]     # Feature names match the training data
)

# Predict using the model
predictions = model.predict(new_data)

# Print results
print("Predictions:", predictions)  # Output: 0 = Normal, 1 = Theft
