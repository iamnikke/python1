# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

input = int(input("Syötä kuhan pituus senttimetreinä: "))
minLength = 37
missingLength = minLength - input
additionalLength = input - minLength

if input < minLength:
    print(input, "cm mittainen kuha on alamittainen.")
    print("Siitä puuttuu", missingLength, "cm")
    print("Heitä kuha takaisin järveen.")
else:
    print("Kuha on riittävän pitkä.")
    if additionalLength > 0:
        print("Se on", additionalLength, "cm minimi mittaa pidempi.")
    else:
        print("Se on tasan minimi mitan pituinen!")

    print("Laita pannulle tirisemään!")
