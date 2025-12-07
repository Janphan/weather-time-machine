from flask import Flask, render_template, jsonify
import pymongo
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
    db = get_db()
    if db is not None:
        collection = db['history']
        latest_data = collection.find_one(sort=[("timestamp", -1)])
        if latest_data:
            return jsonify({
                'temp': latest_data['temp'],
                'condition': latest_data['condition'].capitalize(),
                'timestamp': latest_data['timestamp'].strftime("%d-%m-%Y %H:%M")
            })
    return jsonify({'error': 'No data available'})

if __name__ == '__main__':
    app.run(debug=False)