import requests
import matplotlib.pyplot as plt

# Ask user for a city
city = input("Enter city name: ")

# Fetch data
API_KEY = "77feda0691296b15e78b5c359bd340fa"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# If success
if response.status_code == 200:
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f"City: {city_name}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather: {weather_desc}")

    # Visualize
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [temperature, humidity, wind_speed]
    colors = ['skyblue', 'orange', 'lightgreen']

    plt.bar(labels, values, color=colors)
    plt.title(f"Weather in {city_name}")
    plt.ylim(0, 100)
    plt.ylabel("Value")

    # Save the chart
    plt.savefig(f"weather_{city_name}.png")

    # Show the chart
    plt.show()

else:
    print("City not found or API error.")
