"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla
käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

"""
from unittest import result

import mysql.connector

sqlServer = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="admin",
    password="admin",
    database="flight_game",
    autocommit=True
)



### bonari: ehdota lentokenttää syötteestä jos ei saada muuten osumaa
def suggestIcao(icao):

    # Tietokannan query ja yhteys
    # Poiketen aiemmasta valitse sarakkeet iata_code ja name joihin vertaillaan syötteen KALTAISTA vastausta.
    # Rajoitetaan tulos viiteen spämmin vähentämiseksi
    query = f"SELECT iata_code, name FROM airport WHERE iata_code LIKE '{icao}%' LIMIT 5;"
    cursor = sqlServer.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    # Tulosta ehdotukset
    if cursor.rowcount > 0:

        # Höpöttelyt terminaaliin ensin
        print(f"ICAO-tunniste {icao} ei vastaa lentokenttää. Tarkoititko jotain näistä?")
        # Rivikohtainen käsittely
        for row in result:
            # icao - nimi
            print(">", row[0], "-", row[1])
    # Jos ei pystytä ehdottaa = syöte oli liian pitkä tai se ei vastaa mitään niin virheteksti
    else:
        print("Ei tuloksia.")



### Etsi lentökentän tiedot - aliohjelma
def findAirport(icao):

    # Valitaan lentokentän nimi ja paikkakunta airport-pöydästä missä ident vastaa käyttäjän
    # syöttämää ICAO-tunnistetta
    query = f"SELECT name, municipality FROM airport where ident = '{icao}';"
    # Debug: tulosta wuery
    print("QUERY:", query)
    # Muodostetaan yhteys tietokantaan
    cursor = sqlServer.cursor()
    # Suoritetaan sql-scripti tietokannassa
    cursor.execute(query)
    # haetaan ja tallennetaan tulos result-muuttujaan
    result = cursor.fetchall()

    # Jos tunniste löytää osuman eli rivien määrä on enemmän kuin 0, niin...
    if cursor.rowcount > 0:
        # Tulosta jokaista riviä kohtaan name & municipilaty sarakkeiden arvot:
        for row in result:
            print(f"> ICAO-tunnisteella '{icao}' löytyi lentokenttä: ")
            print("> Lentokentän nimi on", row[0])
            print("> Ja se sijaitsee", row[1])

    # bonus: jos osumia ei tule, niin kutsu toista aliohjelmaa ehdotusten saamiseksi
    elif cursor.rowcount == 0:
        suggestIcao(icao)

    # Palauta kutsuun
    return





### Pääohjelma
while True:

    userInput = str(input("Syötä lentokentän ICAO-tunniste: "))
    # Kutsu aliohjelmaa syöte parametrinä
    findAirport(userInput)