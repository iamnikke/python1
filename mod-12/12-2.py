import requests

api_key = "46467f1acea9144b5bdd0f11571ca41f"

paikkakunta = input("Anna paikkakunnan nimi: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": paikkakunta,
    "appid": api_key,
    "units": "metric",   # Celsius-asteet
    "lang": "fi"         # sään kuvaus suomeksi, jos saatavilla
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    saateksti = data["weather"][0]["description"]
    lampotila = data["main"]["temp"]

    print(f"Säätila: {saateksti}")
    print(f"Lämpötila: {lampotila} °C")
else:
    print("Paikkakuntaa ei löytynyt tai pyyntö epäonnistui.")