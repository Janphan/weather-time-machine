import customtkinter as ctk
import pymongo as pymongo

# 1. GLOBAL SETTINGS
ctk.set_appearance_mode("dark")        # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")    # Themes: "blue" (standard), "green", "dark-blue"

class WeatherDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 2. WINDOW SETUP
        self.title("Weather Analytics")
        self.geometry("500x400")

        # 3. UI ELEMENTS (The Visuals)
        # A. The Title
        self.title_label = ctk.CTkLabel(self, text="Helsinki Weather", font=("Roboto", 24))
        self.title_label.pack(pady=20)

        # B. The Big Temperature
        self.temp_label = ctk.CTkLabel(self, text="--°C", font=("Roboto", 80, "bold"), text_color="#3B8ED0")
        self.temp_label.pack(pady=10)

        # C. The Condition (Cloudy/Sunny)
        self.condition_label = ctk.CTkLabel(self, text="Waiting for data...", font=("Roboto", 18))
        self.condition_label.pack(pady=10)

        self.timestamp_label = ctk.CTkLabel(self, text="", font=("Roboto", 12))
        self.timestamp_label.pack(pady=10)

        # D. The Refresh Button
        self.refresh_btn = ctk.CTkButton(self, text="Refresh Data", width=200, command=self.refresh_data)
        self.refresh_btn.pack(pady=40)

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['weather_app']
        self.collection = self.db['history']


    # 4. BUTTON LOGIC (Placeholder for now)
    def refresh_data(self):
        lastest_data = self.collection.find_one(sort=[("timestamp", -1)])
        if lastest_data:
            self.temp_label.configure(text=f"{lastest_data['temp']}°C")
            self.condition_label.configure(text=lastest_data['condition'].capitalize())
            self.timestamp_label.configure(text=f"Last updated: {lastest_data['timestamp'].strftime("%d-%m-%Y %H:%M")}")
        else:
            self.temp_label.configure(text="--°C")
            self.condition_label.configure(text="No data available.")


if __name__ == "__main__":
    app = WeatherDashboard()
    app.mainloop()