import requests

# 🔐 Replace with your actual OpenWeatherMap API key
API_KEY = "77feda0691296b15e78b5c359bd340fa"

# ⌨️ Take user input for the city
city = input("Enter city name: ")

# 🌐 Form the URL to fetch data (fixed here)
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# 📡 Make the GET request
response = requests.get(url)
data = response.json()

# ✅ Check if the request was successful
if response.status_code == 200:
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']

    # 🖨️ Display weather details
    print(f"\nWeather Report for {city_name}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_desc}")
else:
    # ⚠️ Handle errors
    print("\nFailed to get data. Check your API key or the city name.")
