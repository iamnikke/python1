# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

# Kirjautumistunnukset
username = "moi"
password = "possu"

# Default yritykset 1 kompensoimaan ennen while looppia toteutuneita inputteja.
loginAttempts = 1
# Max
maxLoginAttempts = 5

usernameInput = str(input("Syötä käyttäjänimi: "))
passwordInput = str(input("Syötä salasana: "))

# Kun jompi kumpi on väärin, toista looppia.
while usernameInput != username or passwordInput != password:
    # Kun kirjautumisyritykset on vähemmän kuin maximit
    while loginAttempts < maxLoginAttempts:
        print("Käyttäjätunnus tai salasana väärin.")
        print("Kirjautumisyrityksiä jäljellä:", (maxLoginAttempts - loginAttempts))
        # Lisää kirjautumisyritys
        loginAttempts += 1
        usernameInput = str(input("Syötä käyttäjänimi: "))
        passwordInput = str(input("Syötä salasana: "))

        # Jos kumpikin täsmää muuttujiin -> riko looppi
        if usernameInput == username and passwordInput == password:
            print("Kirjautuminen onnistui")
            break

        # jos kirjautumisyritykset ylittää max rajan -> riko looppi.
        if loginAttempts >= maxLoginAttempts:
            print("Kaikki kirjautumisyritykset käytetty!")
            break