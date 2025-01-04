import pandas as pd
import numpy as np

# Create synthetic data
np.random.seed(42)
rows = 500
data = {
    'PoleID': np.random.randint(1, 3, rows),  # Two poles
    'Voltage': np.random.normal(220, 5, rows),  # Normal voltage around 220V
    'Current': np.random.normal(10, 3, rows),  # Normal current around 10A
    'PowerConsumption': lambda x: x['Voltage'] * x['Current'],  # P = V * I
    'TheftFlag': np.random.choice([0, 1], rows, p=[0.9, 0.1])  # 10% theft cases
}

df = pd.DataFrame(data)
df['PowerConsumption'] = df['Voltage'] * df['Current']

# Add anomalies for theft cases
df.loc[df['TheftFlag'] == 1, 'Current'] += np.random.uniform(5, 15)

# Save data to a CSV file
df.to_csv("electricity_data.csv", index=False)

print("Data generated and saved to electricity_data.csv")
