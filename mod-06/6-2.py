# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

### Funktio / aliohjelma jossa parametrinä tahkojen enimmäismäärä
def rollTheDice(maxAmount):

    # Muuttuja jonka arvo randint:illä 1 - parametrin väliltä.
    diceValue = random.randint(1,maxAmount)
    # Palauta muuttujan arvo kutsuun
    return diceValue

### Pääohjelma

# Kysy tahkojen enimmäismäärä
userInput = int(input("Syötä tahkojen enimmäismäärä: "))

# Ehdollinen while-loop
while True:

    # Määritetään muuttuja joka kutsuu aliohjelmaa
    # Ja antaa parametrinä käyttäjän syöttämän tahkojen enimmäismäärän
    diceValue = rollTheDice(userInput)

    # Jos heitetty tulos on sama kuin tahdojen enimmäismäärä
    if diceValue == userInput:
        # Tulosta jatkettu viesti
        print("Heitit noppaa ja sait luvun ", userInput)
        print("Sait korkeimman mahdollisen tuloksen!")

        # Riko while-loop
        break

    # Jos tulos ei vastannut enimmäismäärää = while-looppia ei rikottu
    # -> Tulosta heitetyn nopan tulos
    print("Heitit noppaa ja sait luvun ", diceValue)



