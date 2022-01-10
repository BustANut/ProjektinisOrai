import requests


def weather(user_input):
    api_key = '88b1bc394b67978e57b52fc12780fe96'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
    if weather_data.json()['cod'] == '404':
        return "404"
    else:
        weather1 = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        pressure = weather_data.json()['main']['pressure'] * 100
        humidity = weather_data.json()['main']['humidity']
        feels_like = round(weather_data.json()['main']['feels_like'])
        return [weather1, temp, pressure, humidity, feels_like]
