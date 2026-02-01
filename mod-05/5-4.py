# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

# Määritetään muuttuja listalle
cityArray = []

# Tehtävän vaatima for-loop nimien kysymiseen:
for i in range(0, 5):

    # Jokaista silmukan kertaa vastaan kerätään kaupungin nimi...
    city = str(input("Syötä kaupungin nimi: "))
    # ... ja lisätään se listaan.
    cityArray.append(city)

# Tulostetaan väliotsikko
print("Syötetyt kaupungit ovat:")

# Lopuksi vielä uusi for-loop tulostamaan listan järjestyksessä 0, 1, 2, 3, 4...
for n in range(0, 5):
    print(cityArray[n])
