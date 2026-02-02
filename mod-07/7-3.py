"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


"""

### Aliohjelma etsii lentokentän
def findAirport():

    # Pyydä ICAO koodi
    icao = str(input("Anna ICAO coodi: "))
    # Jos tietue löytyy sanakirjasta niin kerro sen icao ja nimi
    if icao in airports:
        print(f"ICAO {icao} on lentoasema {airports[icao]}")
    # Palauta kutsulle
    return

### Aliohjelma: luo uuden tietueen
def insertAirport(icao, name):

    # lisätään sanakirjaan icao:name
    airports[icao] = name
    print("Lisätty onnistuneesti")
    return

### Pääohjelma

# Määritetään sanakirjan muuttuja
airports = {}

print("Tervetuloa lentokenttäohjelmaan")
print("Syötä 1 hakeaksesi lentoaseman tiedot")
print("Syötä 2 tallentaaksesi uuden lentoaseman")
print("Syötä 3 lopettaaksesi")

userInput = int(input("Anna numero "))

# while loop toistaa ohjelman valintaa kunnes 3 = lopetetaan -> break
while True:

    # Hae olemassa olevan lentokentän tiedot
    if userInput == 1:

        print("> Haetaan lentoaseman tiedot")
        # Aliohjelman kutsu
        findAirport()

    # Lisää uusi lentokenttä
    elif userInput == 2:

        print("> Tallennetaan uusi lentoasema")
        icao = input("Anna ICAO coodi: ")
        name = input("Anna lentoaseman nimi: ")

        # Aliohjelman kutsu icao + nimi parametreillä
        insertAirport(icao, name)

    # Lopeta ohjelma breakillä
    elif userInput == 3:

        print("> Lopetetaan ohjelma")
        break

    # Muuten syötetty toiminnon numero oli virheellinen -> virheteksti ja ohjelma jatkuu
    else:
        print("Virheellinen ohjelma!")

    # while loop toistaa aina tätä inputtia jos sitä ei ole rikottu.
    userInput = int(input("Anna numero "))
