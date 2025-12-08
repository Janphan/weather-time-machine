from flask import Flask, render_template, jsonify, request
import pymongo
import requests
import os
from dotenv import load_dotenv

load_dotenv()

from backend import MONGO_URI  # Import from backend.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# MongoDB Setup (moved inside routes to avoid startup crash)
def get_db():
    try:
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'), tls=True)
        db = client['weather_app']
        return db
    except Exception as e:
        print(f"DB connection error: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    city = request.args.get('city')
    if city:
        # Fetch live weather for the selected city
        api_key = os.environ.get('API_KEY')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return jsonify({
                    'temp': data['main']['temp'],
                    'condition': data['weather'][0]['description'].capitalize(),
                    'city': data['name']
                })
            else:
                return jsonify({'error': 'City not found or API error'})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        # Fetch latest from DB for default city
        db = get_db()
        if db is not None:
            collection = db['history']
            latest_data = collection.find_one(sort=[("timestamp", -1)])
            if latest_data:
                return jsonify({
                    'temp': latest_data['temp'],
                    'condition': latest_data['condition'].capitalize(),
                    'timestamp': latest_data['timestamp'].strftime("%d-%m-%Y %H:%M"),
                    'city': 'Helsinki'  # Default city
                })
        return jsonify({'error': 'No data available'})
if __name__ == '__main__':
    app.run(debug=False)