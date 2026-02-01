# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

# Määritetään muuttujat
userInput = str(input('Syötä luku: '))
intArray = []

# Niin kauan kun input ei ole tyhjä
while userInput != '':

    # Konvertoi syöte kokonaisluvuksi int
    userInput = int(userInput)
    # Lisää luku listaan
    intArray.append(userInput)
    # Luo uus input joka kysyy seuraavaa lukua
    userInput = str(input('Syötä luku: '))

# Järjestä lista suurimmasta pienimpään.
intArray.sort(reverse=True)

# Jokaista ALKOITA vastaan listan 1-5 itemeistä, tulosta luku
for userInput in intArray[:5]:
    print(userInput)
