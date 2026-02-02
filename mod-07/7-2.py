"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.

"""

userInput = str(input("Syötä nimi: "))

# Muuttuja nimien joukkotietorakenteelle
names = set()

### while looppi kunnes input on tyhjä
while userInput != "":

    # Jos nimi löytyy jo listasta, anna virheteksti äläkä lisää sitä listalle
    if userInput in names:
        print("VIRHE: Aiemmin syötetty nimi")

    # Nimeä ei ole vielä listassa -> success teksti ja lisää se listalle
    else:
        print("LISÄTTY: Uusi nimi")
        names.add(userInput)

    # Kysy uutta nimeä
    userInput = str(input("Syötä nimi: "))

### while loop mennyt rikki = eli syöte ollut tyhjä
### -> for-loop jokaista nimeä kohtaan listassa
for name in names:
    # Tulosta yksittäinen nimi
    print(name)
