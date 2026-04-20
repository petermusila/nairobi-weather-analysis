import json
import pandas as pd

# Load the JSON file
with open("nairobi_weather.json", "r") as file:
    data = json.load(file)

# Extract hourly data
hourly = data["hourly"]

# Create DataFrame
df = pd.DataFrame({
    "timestamp": hourly["time"],
    "temperature_c": hourly["temperature_2m"],
    "humidity_percent": hourly["relative_humidity_2m"],
    "rain_mm": hourly["rain"],
    "wind_speed_kmh": hourly["wind_speed_10m"]
})

# Save to CSV
df.to_csv("nairobi_weather.csv", index=False)

print("Conversion complete!")
print(f"Saved {len(df)} rows to nairobi_weather.csv")
print("\nFirst 5 rows:")
print(df.head())