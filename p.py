import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Using metric units
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the response contains valid data
        if response.status_code == 200:
            main = data["main"]
            weather = data["weather"][0]
            print(f"\nWeather in {city.capitalize()}:")
            print(f"Temperature: {main['temp']:.2f}°C")
            print(f"Description: {weather['description'].capitalize()}")
        elif data["cod"] == "404":
            print("\nCity not found!")
        else:
            print("\nAn error occurred:", data["message"])
            
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error: {e}")

# Get user input
city_name = input("Enter city name: ")
get_weather(city_name)
