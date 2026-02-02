"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

"""

# Vuodenajan labelit määritetty tähän helpomman hallinnan vuoksi
seasonLabels = (
    "Talvi",
    "Kevät",
    "Kesä",
    "Syksy"
)

# Monikot kuukausille
winterMonths = (12, 1, 2)
springMonths = (3, 4, 5)
summerMonths = (6, 7, 8)
autumnMonths = (9, 10, 11)

userInput = int(input("Syötä kuukauden numero: "))

while userInput != 0:
    if userInput in winterMonths:

        # Hae vuodenajan TALVI label
        currentSeason = seasonLabels[0]
        print("Syöttämäsi kuukausi kuuluu vuodenaikaan " + currentSeason)

        # Pyydä uusi kuukausi
        userInput = int(input("Syötä kuukauden numero: "))

    elif userInput in springMonths:

        # Hae vuodenajan KEVÄT label
        currentSeason = seasonLabels[1]
        print("Syöttämäsi kuukausi kuuluu vuodenaikaan " + currentSeason)

        # Pyydä uusi kuukausi
        userInput = int(input("Syötä kuukauden numero: "))

    elif userInput in summerMonths:

        # Hae vuodenajan KESÄ label
        currentSeason = seasonLabels[2]
        print("Syöttämäsi kuukausi kuuluu vuodenaikaan " + currentSeason)

        # Pyydä uusi kuukausi
        userInput = int(input("Syötä kuukauden numero: "))

    elif userInput in autumnMonths:

        # Hae vuodenajan SYKSY label
        currentSeason = seasonLabels[3]
        print("Syöttämäsi kuukausi kuuluu vuodenaikaan " + currentSeason)

        # Pyydä uusi kuukausi
        userInput = int(input("Syötä kuukauden numero: "))

# Kuukausi ei ollut 1-12
    else:
        print("heippa")
        break