# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

diceAmount = int(input('Anna arpakuutioiden määrä: '))

# Määritetään noppien kokonaissumman muuttuja.
totalDiceValue = 0

# For silmukka 1 -> Käyttäjän syöttämä noppien määrä.
# +1 sen takia, että tulostetut nopan numerot menee oikein. Voisi olla myös range(0, diceAmount):
for diceAmount in range(1, diceAmount + 1):

    # Yksittäisen nopan arvo randomisti
    diceValue = random.randint(1, 6)

    # Tulostetaan se muuten vaa läpäl
    print('Noppa numero', diceAmount, 'heittää luvun', diceValue)

    # Lisätään noppien kokonaissummaan juuri heitetyn nopan arvo
    totalDiceValue = totalDiceValue + diceValue

# Kun for silmukka on valmis niin tulostetaan kokonaissumma.
print('Kaikkien noppien summa on:', totalDiceValue)