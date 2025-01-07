import numpy as np
import pandas as pd

# Function to generate synthetic data
def generate_theft_dataset(num_samples=10000):
    voltage = []
    current = []
    power = []
    theft = []

    for _ in range(num_samples):
        if np.random.rand() > 0.3:  # 70% chance for normal load
            # Normal Load: 2 LEDs (2.4W, 12V each) connected in parallel
            v = np.random.uniform(11.5, 12.5)  # Slight voltage variation
            i = np.random.uniform(0.38, 0.42)  # Current for 2 LEDs (0.4A nominal)
            p = v * i  # Power calculation
            t = 0  # Normal load
        else:  # Theft scenario
            # Normal Load + Theft Load (e.g., an external LED, 12V 5W)
            v = np.random.uniform(11.5, 12.5)  # Voltage variation
            i = np.random.uniform(0.8, 0.85)  # Increased current due to theft load
            p = v * i  # Power calculation
            t = 1  # Theft load

        voltage.append(v)
        current.append(i)
        power.append(p)
        theft.append(t)

    # Create a DataFrame
    data = pd.DataFrame({
        'voltage': voltage,
        'current': current,
        'power': power,
        'theft': theft
    })

    return data

# Generate the dataset
dataset = generate_theft_dataset(10000)

# Save the dataset to a CSV file
dataset.to_csv('electricity_theft_data.csv', index=False)

print("Dataset generated and saved as 'electricity_theft_data.csv'.")
