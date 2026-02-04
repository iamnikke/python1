"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että
pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

"""
import mysql.connector


### Sql ytheyden tiedot
sqlServer = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="admin",
    password="admin",
    database="flight_game"
)



###
def countAirportViaTypes(iso_country):

    query = f"SELECT type, COUNT(*) AS amount FROM airport WHERE iso_country = '{iso_country}' GROUP BY type"
    cursor = sqlServer.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:

        if row[0] == "closed":
            print("Suljettuja lentokenttiä", row[1], "kappaletta")

        elif row[0] == "heliport":
            print("Helikopterikenttiä", row[1], "kappaletta")

        elif row[0] == "large_airport":
            print("Suuria lentokenttiä", row[1], "kappaletta")

        elif row[0] == "medium_airport":
            print("Keskikokoisia lentokenttiä", row[1], "kappaletta")

        elif row[0] == "small_airport":
            print("Pieni lentokenttiä", row[1], "kappaletta")




### PÄÄOHJELMA
while True:
    userInput = str(input("Syötä maatunnus: "))
    countAirportViaTypes(userInput)


