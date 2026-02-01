# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

### Aliohjelma
### Hyväksyy parametrinä listan numberoita
def numbers(numbersArray):

    # Määritetään summan muuttuja
    numbersTotalSum = 0

    # for-loop jokaiselle listan numerolle
    for number in numbersArray:
        # Lisää numeron arvo summan muuttujaan.
        numbersTotalSum += number

    # Palauta kokonaissumma kutsulle
    return numbersTotalSum



### Pääohjelma

print("Lasketaan lukujen summa.")
print("Anna luku 0 suorittaaksesi laskun aliohjelmassa.")
# Kysy luku
userInput = int(input("Syötä luku: "))

# Määritetään muuttuja listalle
numbersArray = []

# while-loop: niin pitkään kun syöte on enemmän kuin 0
while userInput > 0:
    # Tulosta annettu luku
    print("Annoit luvun", userInput)
    # Lisää annettu luku listaan
    numbersArray.append(userInput)
    # Tulosta listan nykyinen tilanne
    print("Listassa on nyt luvut", numbersArray)

    #Pyydä uutta lukua
    userInput = int(input("Syötä luku: "))
else:
    # Muuttuja joka kutsuu aliohjelmaa lista parametrinään
    numbersSum = numbers(numbersArray)
    # Tulosta summa
    print("Yhteenlaskettu summa on", numbersSum)