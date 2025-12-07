from flask import Flask, render_template, jsonify
import pymongo
from backend import MONGO_URI  # Import from backend.py

app = Flask(__name__)

# MongoDB Setup
client = pymongo.MongoClient(MONGO_URI)
db = client['weather_app']
collection = db['history']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    latest_data = collection.find_one(sort=[("timestamp", -1)])
    if latest_data:
        return jsonify({
            'temp': latest_data['temp'],
            'condition': latest_data['condition'].capitalize(),
            'timestamp': latest_data['timestamp'].strftime("%d-%m-%Y %H:%M")
        })
    return jsonify({'error': 'No data available'})

if __name__ == '__main__':
    app.run(debug=True)