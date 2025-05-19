import requests
import random
import time

url = "https://us-central1-fleet-monitoring-project.cloudfunctions.net/predict_vehicle_failure_http"

def generate_data():
    return {
        "vehicle_id": f"V{random.randint(1000, 9999)}",
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "engine_temp": random.uniform(70, 130),
        "oil_pressure": random.uniform(15, 40),
        "tire_pressure": random.uniform(20, 40),
        "battery_voltage": random.uniform(10, 14),
        "latitude": 42.2808,
        "longitude": -83.7430
    }

def main():
    while True:
        data = generate_data()
        try:
            response = requests.post(url, json=data)
            print(f"Sent: {data} | Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(10)

if __name__ == "__main__":
    main()
