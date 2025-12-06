import requests
import pymongo
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.environ.get('API_KEY')
CITY = os.getenv("CITY")
MONGO_URI = os.getenv("MONGO_URI")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

client = pymongo.MongoClient(MONGO_URI)

db = client['weather_app']

collection = db['history']

def fetch_and_save():
    print(f"Fetching weather for {CITY}...")
    
    try:
        response = requests.get(URL)
        
        if response.status_code == 200:
            data = response.json()
            print(data)  # For debugging purposes
            
            weather_doc = {
                "city": data['name'],
                "temp": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "humidity": data['main']['humidity'],
                "condition": data['weather'][0]['description'],
                "timestamp": datetime.now()  # Adds the exact time
            }
            
            collection.insert_one(weather_doc)
            print("✅ Data saved to MongoDB successfully!")
            print(f"Saved Document: {weather_doc}")
            
        else:
            print(f"❌ API Error: {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print(f"Weather Worker started for {CITY}...")
    print("Press Ctrl+C to stop.")
    while True:
        fetch_and_save()
        time.sleep(3600)  # Wait for 1 hour before fetching again