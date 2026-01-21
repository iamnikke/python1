# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

# Muuttujat mistä mihin
valueMin = 1
value = 1000

while value >= valueMin:
    # Jakojäännös, jos jäljelle 0 niin on jaollinen kolmella.
    if value % 3 == 0:
        print(value)
        value -= 1
    # Jos ei jaollinen niin vähennä yksi
    else:
        value -= 1