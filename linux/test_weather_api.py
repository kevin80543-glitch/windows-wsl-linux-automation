import csv
import requests
import logging
from datetime import datetime

def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=25.03"
        "&longitude=121.56"
        "&current_weather=true"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def transform_weather(raw_data):
    cw = raw_data["current_weather"]

    return {
        "timestamp": cw["time"],
        "temperature_c": cw["temperature"],
        "windspeed_kmh": cw["windspeed"],
        "winddirection_deg": cw["winddirection"],
        "is_day": cw["is_day"],
        "created_at": datetime.utcnow().isoformat()
    }

def save_to_csv(record, filename="weather_output.csv"):
    fieldnames = list(record.keys())

    file_exists = False
    try:
        with open(filename, "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(record)

def main():
    logging.basicConfig(
        filename="/mnt/c/Users/<username>/Desktop/mis_output/weather.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        raw = fetch_weather()
        record = transform_weather(raw)
        save_to_csv(record, filename="/mnt/c/Users/<username>/Desktop/mis_output/weather_output.csv")
        logging.info(f"SUCCESS: Saved record {record}")
        print("Saved weather record:", record)
    except Exception as e:
        logging.error(f"ERROR: {str(e)}")
        print("Error occurred:", e)

if __name__ == "__main__":
    main()

