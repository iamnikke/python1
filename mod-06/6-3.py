# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


### Aliohjelma joka hyväksyy parametriksi gallonat
def transformGalToL(amountGal):
    # Muunnos
    amountLiters = amountGal * 3.785
    # Palauta muunnos kutsulle
    return amountLiters


### Pääohjelma

userInput = int(input("Syötä gallonat: "))

# while-loop: niin kauan sun syötetyt gallonat ovat 0 tai enemmän, eli positiivinen luku
while userInput >= 0:
    # Muuttuja joka kutsuu aliohjelmaa
    amountLiters = transformGalToL(userInput)
    # Tulosta käyttäjän syöttämät gallonat ja aliohjelman palauttama muunnos
    print(userInput, "gallonaa on", amountLiters, "litraa.")

    # Jatka ohjelmaa pyytämällä uudet gallonat
    userInput = int(input("Syötä gallonat: "))

# While-loop on rikottu eli syöte oli negatiivinen, tulosta heipat.
print("Syötit negatiivisen luvun. Ohjelma loppui. Heippa.")