from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()

def get_current_weather(city = 'Toronto'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
    result = requests.get(request_url).json()
    return result


# if the file is called directly in the terminal [python3 weather.py]
if __name__ == "__main__":
    print('\n  Get Current Weather Condition \n')
    city = input('\n Please enter a city name: \n')
    # Check for an empty string
    if city.strip() == ' ' or len(city) == 0:
        city = 'Toronto'
    weather_data = get_current_weather(city)
    pprint(weather_data)