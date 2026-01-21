# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

value = str(input("Syötä numero: "))

# Määritetään muuttujat
valueMin = int(value)
valueMax = int(value)

# Niin pitkään kun syöte ei ole tyhjä merkkijono, niin toista seuraava lohko.
while value != "":

    # Konvertoi string input integeriksi.
    value = int(value)

    # Jos syöte on suurempi kuin maksimi muuttuja, niin korvaa se uudella.
    if value > valueMax:
        valueMax = value
    # -||- sama toistepäi :)
    elif value < valueMin:
        valueMin = value

    # Pyydä uusi input
    value = str(input("Syötä numero: "))

# Jos input on tyhjä merkkijono, lopeta ohjelma ja tulosta min, max ja heipat.
else:
    print("Tyhjä merkkijono. Lopetetaan ohjelma.")
    print("Pienin luku oli:", valueMin)
    print("Suurin luku oli:", valueMax)