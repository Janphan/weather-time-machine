# Weather Analytics Dashboard 🌦️

A full-stack Python application that logs real-time weather data to a NoSQL database and visualizes it in a modern web dashboard.

**Live Demo:** [https://weather-time-machine-app-6c83b70b9faf.herokuapp.com/](https://weather-time-machine-app-6c83b70b9faf.herokuapp.com/)

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Database:** MongoDB (Time-Series Data)
- **Frontend:** HTML/CSS/JavaScript (Responsive Web UI)
- **Backend:** Flask (Web Framework)
- **API:** OpenWeatherMap

## 🚀 How to Run Locally

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Create a `.env` file in the root directory with:

   ```
   API_KEY=your_openweathermap_api_key
   CITY=your_city_name
   MONGO_URI=your_mongodb_connection_string
   ```

3. **Start the Backend (Data Fetcher):**

   ```bash
   python backend.py
   ```

   This runs in the background, fetching weather data every hour.

4. **Launch the Web Dashboard:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000/` in your browser.

## 🌐 Deployment to Heroku

1. **Install Heroku CLI** and log in:

   ```bash
   heroku login
   ```

2. **Create Heroku App:**

   ```bash
   heroku create your-app-name
   ```

3. **Add Files:**

   - Ensure `requirements.txt` includes all dependencies (run `pip freeze > requirements.txt`).
   - Create `Procfile`:
     ```
     web: python app.py
     ```

4. **Deploy:**

   ```bash
   git add .
   git commit -m "Deploy web app"
   git push heroku main
   ```

5. **Access:** Visit the Heroku-provided URL.

## 📊 Features

- Real-time weather data fetching and storage.
- Responsive web dashboard with auto-refresh.
- Temperature-based color coding (blue for cold, green for moderate, red for hot).
- Minimal black-and-white design.

## 🔧 Environment Variables

- `API_KEY`: OpenWeatherMap API key.
- `CITY`: City for weather data (e.g., Helsinki).
- `MONGO_URI`: MongoDB connection string.

## 📝 Notes

- The backend (`backend.py`) should run continuously for data logging.
- For production, consider using a scheduler (e.g., Heroku Scheduler) for the backend.
- Free Heroku tier has usage limits; monitor dyno hours.
