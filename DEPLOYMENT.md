# Quick Setup and Deployment Guide

This guide provides step-by-step instructions to set up and deploy the Weather Analytics Dashboard to Heroku.

## Prerequisites

- Python 3.10+ installed locally
- Heroku CLI installed (`npm install -g heroku` or download from Heroku site)
- MongoDB Atlas account (free tier at mongodb.com/atlas)
- OpenWeatherMap API key (free at openweathermap.org)

## Required Files

Before starting, ensure these files exist in your project root:

- `app.py` (Flask web app)
- `backend.py` (Data fetcher)
- `requirements.txt` (Dependencies: flask, pymongo[srv], python-dotenv, requests, gunicorn)
- `Procfile` (Contains: `web: gunicorn wsgi:app`)
- `wsgi.py` (WSGI entry point)
- `templates/index.html` (Web UI)
- `.env` (Local environment variables, not committed)

## Step 1: Local Setup

1. **Clone or navigate to the project:**

   ```bash
   cd /path/to/weather_time-machine
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   - Create a `.env` file in the root:
     ```
     API_KEY=your_openweathermap_api_key
     CITY=Helsinki
     MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?appName=Cluster0
     ```
   - Get API key from OpenWeatherMap.
   - Set up MongoDB Atlas: Create cluster, user, and get URI.

4. **Test locally:**
   - Run backend: `python backend.py` (fetches data every hour).
   - Run web app: `python app.py` (visit http://127.0.0.1:5000/).
   - Check for errors in console.

## Step 2: Prepare for Heroku

1. **Install Heroku CLI and log in:**

   ```bash
   heroku login
   ```

2. **Create Heroku app:**

   ```bash
   heroku create your-unique-app-name
   ```

3. **Set environment variables on Heroku:**

   ```bash
   heroku config:set API_KEY=your_api_key
   heroku config:set CITY=Helsinki
   heroku config:set MONGO_URI=your_mongodb_atlas_uri
   ```

4. **Ensure Atlas allows Heroku IPs:**
   - In Atlas > Network Access, add IP: `0.0.0.0/0`.

## Step 3: Deploy to Heroku

1. **Commit changes:**

   ```bash
   git add .
   git commit -m "Ready for deployment"
   ```

2. **Push to Heroku:**

   ```bash
   git push heroku main
   ```

3. **Open the app:**
   ```bash
   heroku open
   ```

## Debugging and Troubleshooting

- **App crashes (503 error):** Check logs: `heroku logs --tail`. Common issues: Invalid MONGO_URI, missing dependencies.
- **No data displayed:** Run `python backend.py` locally to populate DB, or set up Heroku Scheduler for automated runs.
- **Build fails:** Ensure `requirements.txt` is updated and `Procfile` is correct.
- **Local issues:** Verify `.env` variables and Python version (3.10+).
- **Atlas connection:** Test URI locally with `python backend.py`.

## Important Notices

- **Security:** Never commit API keys or sensitive data. Use Heroku config vars for secrets.
- **Costs:** Free tiers (Heroku, Atlas) have limits. Monitor usage to avoid charges.
- **Data Privacy:** Ensure compliance with data laws (e.g., GDPR) if handling user data.
- **Scalability:** For high traffic, upgrade Heroku dynos and Atlas clusters.
- **Backups:** Regularly back up MongoDB data via Atlas.
- **Updates:** Keep dependencies updated for security patches.

## Notes

- The backend isn't deployed; run it locally or use Heroku Scheduler.
- Free Heroku tier sleeps after inactivity; pro tier for always-on.
- For production, disable debug mode and use HTTPS.

For detailed docs, see README.md.
