from flask import Flask, request
import csv
import os

app = Flask(__name__)

# CSV file path
csv_file_path = "sensor_data.csv"

# Ensure the CSV file exists
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["current", "voltage", "reading", "flag", "info"])

@app.route('/store-data', methods=['POST'])
def store_data():
    # Get data from the POST request
    current = request.form.get("current")
    voltage = request.form.get("voltage")
    reading = request.form.get("reading")
    flag = request.form.get("flag")
    info = request.form.get("info")

    # Validate data
    if not all([current, voltage, reading, flag, info]):
        return "Invalid data", 400

    # Append data to the CSV file
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([current, voltage, reading, flag, info])

    return "Data stored successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
