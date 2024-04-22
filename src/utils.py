import requests
import dotenv
import os
import objc
from CoreLocation import CLLocationManager, CLGeocoder, CLLocation
import time 

dotenv.load_dotenv()

def get_current_location():
    # Initialize CLLocationManager
    manager = CLLocationManager.alloc().init()
    # Set delegate to self (CLLocationManagerDelegate)
    manager.setDelegate_(manager)  

    # Request authorization
    manager.requestWhenInUseAuthorization()
    manager.startUpdatingLocation()

    # Wait for the location to be updated
    max_wait_time = 10
    start_time = time.time()
    while manager.location() is None and time.time() - start_time < max_wait_time:
        pass

    if manager.location():
        # Get latitude and longitude
        latitude = manager.location().coordinate().latitude
        longitude = manager.location().coordinate().longitude
        return latitude, longitude
    else:
        print("Failed to get current location.")
        return None, None

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    city = city
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(url)
    data = response.json()

    if "error" not in data:
        weather_description = data["current"]["condition"]["text"]
        temperature_c = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        return f"The weather in {city} is {weather_description}. The temperature is {temperature_c} degrees celcius. Current humidity level is at {humidity}%. Wind speed is at {wind_kph} kilometers per hour."
    else:
        return f"Sorry, I could not access the weather information for {city}."

