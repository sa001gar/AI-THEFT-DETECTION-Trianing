from flask import Flask, request, jsonify
import numpy as np
import pickle

# Load the trained AI model
model_file = "theft_detection_model.pkl"  # Path to your trained model
with open(model_file, "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Endpoint to receive data from ESP32
@app.route('/send-data', methods=['POST'])
def receive_data():
    try:
        # Parse JSON data from ESP32
        data = request.json
        current = data.get('current')  # Current in amperes
        voltage = data.get('voltage')  # Voltage in volts

        # Ensure valid data is received
        if current is None or voltage is None:
            return jsonify({"status": "error", "message": "Invalid data"}), 400

        # Prepare data for the model
        input_data = np.array([[current, voltage]])

        # Make a prediction
        prediction = model.predict(input_data)

        # Map the prediction to the response
        theft_detected = bool(prediction[0])  # 1 indicates theft, 0 indicates normal

        if theft_detected:
            message = "Electricity theft detected!"
        else:
            message = "No theft detected."

        # Send response back to ESP32
        return jsonify({"status": "success", "theft_detected": theft_detected, "message": message})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
