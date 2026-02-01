# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

userInput = int(input("Syötä luku: "))

# for-loop käy läpi kaikki jakajat 2 - käyttäjän syöttämän luvun väliltä.
for i in range(2, userInput):

    # Jos jakojäännös menee tasan siltä väliltä, niin luku ei ole alkuluku.
    if userInput % i == 0:
        print("Ei alkuluku")
        break

# Jos jakojäännös ei mene tasan millään jakajalla rangesta, silloin kyseessä on alkuluku
# koska se on jaollinen vain yhdellä ja itsellään.
else:
    print("Alkuluku")
