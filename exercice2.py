from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '7e6198eedd7e694a19f6466a6469741a'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):    
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric" # Construire l'URL de la requête
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extraire les informations météorologiques
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        return {"error": "City not found or API request failed"}

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        weather_info = fetch_weather(city)
        return jsonify(weather_info)
    else:
        return jsonify({"error": "City parameter is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)
