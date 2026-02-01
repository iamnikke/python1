# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

### Aliohjelma, parametreinä halkaisija ja hinta

def pizzaCalculator(diameter, price):

    # Laske säde jakamalla halkaisija
    pizzaRadius = diameter / 2
    # Laske pinta-ala pii * säde^2
    pizzaAreaCm2 = math.pi * pizzaRadius**2

    # Muunna cm2 -> m2
    pizzaAreaM2 = pizzaAreaCm2 / 10000

    # laske hinta per m2
    pizzaPricePerM2 = price / pizzaAreaM2

    # palauta neliömetrin hinta kutsulle
    return pizzaPricePerM2




### Pääohjelma

# Muuttujat paremmalle pizzalle
betterChoice = 0
betterPrice = 0

# Montako pizzaa vertaillaan?
pizzaAmount = 2

#for silmukka
for i in range (0,pizzaAmount):

    # Tilanjakaja terminaalissa
    print("========================================")

    # Kysy pizzan halkaisija + hinta
    inputDiameter = float(input("Anna ympyrän halkaisija (cm): "))
    inputPrice = float(input("Anna pizzan hinta (esim 5.50€):"))

    # Kutsu aliohjelmaa parametreillä
    pizzaPrice = pizzaCalculator(inputDiameter, inputPrice)
    # Tulosta aliohjelman palauttama tulos
    print(f"> Pizzan metrihinta: {pizzaPrice:.2f} €/m²")

    # Jos pizzan metrihinta on pienempi kuin muuttujaan määritetty hinta
    # TAI jos nykyinen muuttujan hinta on 0, eli kyseessä on ensimmäisen pizzan käsittely
    # -> niin korvaa muuttuja pizzan hinnalla
    if pizzaPrice < betterPrice or betterPrice == 0:
        betterPrice = pizzaPrice
        betterChoice = i

## Lopputekstit

# Tilanjakaja terminaalissa
print("========================================")

# BONUS: käyttäjäystävälliset tekstit ;D
betterChoiceUserFriendly = ""
if betterChoice == 0:
    betterChoiceUserFriendly = "ensimmäisellä"
elif betterChoice == 1:
    betterChoiceUserFriendly = "jälkimmäisellä"


print("Enemmän vastinetta rahalle saat " + betterChoiceUserFriendly + " pizzalla")
print(f"> Pizzan metrihinta {betterChoiceUserFriendly} pizzalla oli: {betterPrice:.2f} €/m²")