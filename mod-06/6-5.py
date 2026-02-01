# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi
# että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.


### Aliohjelma, parametrinä lista
def parseOddIntegers(numbersArray):

    # for-loop: jokaista listan alkiota kohtaan
    for number in numbersArray:

        # jos numero ei ole jaollinen kahdella niin...
        if number % 2 != 0:

            # ...poista numero listasta
            numbersArray.remove(number)

    # palauta karsittu lista kutsulle
    return numbersArray


### Pääohjelma

# Alkusanat
print("Karsitaan parittomat luvut pois.")
print("Syötä luku 0 kutsuaksesi aliohjelmaa.")

#
userInput = int(input("Anna luku: "))

# Määritetään listan muuttuja
numbersArray = []

# while-loop: niin pitkään kun syöte on 1 tai enemmän...
while userInput > 0:

    # Tulosta minkä luvun käyttäjä syötti
    print("Annoit luvun", userInput)
    # Lisää luku listaan
    numbersArray.append(userInput)
    # Tulosta listan nykyset luvut
    print("Listassa on nyt luvut", numbersArray)
    # Pyydä uutta lukua
    userInput = int(input("Anna luku: "))

# input on ollut 0 tai alle = else
else:

    # Tulostetaan nykyinen lista kaikilla luvuilla
    print("Listassa on nyt luvut", numbersArray)

    # korvataan listan muuttuja aliohjelman kutsulla, joka palauttaa listan vain parillisilla luvuilla
    # (korvataan nyt koska sille ei ole muutakaan käyttöä enää tässä ohjelmassa = hienosti optimoitu ohjelma)
    numbersArray = parseOddIntegers(numbersArray)
    print("Karsittu lista parillisia lukuja on", numbersArray)