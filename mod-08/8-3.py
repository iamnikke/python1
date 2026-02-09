"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

"""
import mysql.connector
from geopy import distance

# Tietokannan yhteys
db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="admin",
    password ="admin",
    database="flight_game"
)

def calculateDistance(icao1, icao2):

    # Kysely: valitse ICAO vastaavuudets
    query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE iata_code = '{icao1}' OR iata_code = '{icao2}'"
    # MUodosta yhteys tietokantaan
    cursor = db.cursor()
    # Suorita kysely
    cursor.execute(query)
    # Nouda tulokset
    result = cursor.fetchall()

    # Muuttujat
    # AirportData = sanakirja joka säilöö koordinaatit
    airportData = {}
    # indeksi jota käytetään for loopissa
    i = 1

    # For-loop tulosten lokeroimiseksi
    for row in result:
        # Lisää tuloksen koordinaatit sanakirjaan
        airportData[i] = row[0], row[1]
        # Nosta indeksiä seuraavan rivin käsittelyksi
        i += 1

    # debug viesti
    print("DEBUG: Sanakirjaan tallennettu: ", airportData)

    # Geopyn distance-funktio mille annetaan sanakirjan koordinaatit parametreinä
    geopyDistance = distance.distance(airportData[1], airportData[2])
    # Tulosta koordinaattien välinen etäisyys
    print(geopyDistance)




### Pääohjelma
# Kutsu funktiota lentokenttien ICAO koodeilla.
calculateDistance("HEL", "BRU")

