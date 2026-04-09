import requests

# Haetaan satunnainen vitsi API:sta
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

# Muutetaan vastaus JSON-muotoon
data = response.json()

# Tulostetaan pelkkä vitsin teksti
print(data["value"])