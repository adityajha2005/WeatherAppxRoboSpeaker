import requests
import json
import win32com.client as wincom

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=c0d1e20bb09d4b6abe524532241405&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to retrieve weather data for {city}.")
        return None

def speak_weather(city, weather_data):
    if weather_data:
        location = weather_data["location"]["name"]
        local_time = weather_data["location"]["localtime"]
        temperature_c = weather_data["current"]["temp_c"]
        temperature_f = weather_data["current"]["temp_f"]
        is_day = "day" if weather_data["current"]["is_day"] == 1 else "night"

        speak = wincom.Dispatch("SAPI.SpVoice")
        text = f"Weather in {location} at local time {local_time} is {temperature_c} degrees Celsius and {temperature_f} degrees Fahrenheit. It's currently {is_day}."
        speak.Speak(text)
        print(text)
    else:
        print("No weather data available.")

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    weather_data = get_weather(city)
    speak_weather(city, weather_data)
