import requests

api_key = "5eb968afee9538911b09e4d76a7390ea"   


def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # Corrected to 'metric'

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"City: {city}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found")   

def get_weather_forecast(city):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"  # Corrected to use the forecast endpoint
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # Corrected to 'metric'

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather forecast for {city}:")
        
        for forecast in data['list'][:4]:  # Get the first 4 forecast entries
            temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"Temp: {temperature}, Desc: {description}")
    else:
        print("City not found")       

city = input("Enter the city: ")
get_weather(city)
get_weather_forecast(city)
