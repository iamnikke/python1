# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

### rändöm luvun arvonta funktio
def randomInt():

    # Arpoo random luvun randint() avulla
    randomInt = random.randint(1, 6)

    # Palauta arvottu luku kutsuun
    return randomInt

#### PÄÄOHJELMA

# Määritä muuttuja nopan arvolle ja kutsu aliohjelmaa
diceValue = randomInt()

# Tulosta aliohjelman palauttama arvo
print(diceValue)

# While-loop niin pitkään kun aliohjelman palauttama arvo ei ole 6
while diceValue != 6:

    # Määritetään muuttujan arvo uudestaan kutsumalla aliohjelmaa
    diceValue = randomInt()
    # TUlosta uusi arvo
    print(diceValue)

# While-loop on rikkoutunut kun päästään tänne asti = tulostetaan onnittelut
print("Heitit kutosen - onnittelut")
