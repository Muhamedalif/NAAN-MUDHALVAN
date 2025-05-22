import random
import pandas as pd
import matplotlib.pyplot as plt

# Sample historical data for disasters
data = {
    'Year': list(range(2010, 2025)),
    'Earthquake_Risk': [random.uniform(0.1, 0.9) for _ in range(15)],
    'Flood_Risk': [random.uniform(0.2, 0.95) for _ in range(15)],
    'Wildfire_Risk': [random.uniform(0.05, 0.85) for _ in range(15)]
}

df = pd.DataFrame(data)

# Prediction Logic: Simple threshold-based
def predict_disaster_risk(row):
    alerts = []
    if row['Earthquake_Risk'] > 0.7:
        alerts.append("Earthquake Alert")
    if row['Flood_Risk'] > 0.8:
        alerts.append("Flood Alert")
    if row['Wildfire_Risk'] > 0.75:
        alerts.append("Wildfire Alert")
    return alerts

# Apply prediction
df['Alerts'] = df.apply(predict_disaster_risk, axis=1)

# Management: Display alerts
def display_alerts(df):
    print("\n--- Disaster Alerts ---")
    for index, row in df.iterrows():
        if row['Alerts']:
            print(f"Year {row['Year']}: {', '.join(row['Alerts'])}")

# Visualization
def visualize_risks(df):
    df.set_index('Year')[['Earthquake_Risk', 'Flood_Risk', 'Wildfire_Risk']].plot(
        title="Disaster Risk Prediction Over Years", figsize=(10, 5))
    plt.ylabel("Risk Level")
    plt.show()

if _name_ == "_main_":
    display_alerts(df)
    visualize_risks(df)