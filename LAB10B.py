
weather_data = {
    "main": {
        "temp": 15.45,  # Replace with the actual temperature
        "humidity": 64,  # Replace with the actual humidity
    },
    "weather": [
        {
            "description": "clear",  # Replace with the actual weather description
        }
    ]

}


current_temp = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
weather_desc = weather_data['weather'][0]['description']

print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")
