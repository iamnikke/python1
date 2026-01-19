# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

input = int(input("Syötä vuosi: "))

# Oletan, että tehtävässä ei hyväksytä jaollisuusvertailua modulolla (%), joten tein tälläisen vertailun..

# Vertaile input jaettuna 4 vs input jaettuna 4 kokonaislukuna.
# Jos luvut täsmää, vuosiluku on jaollinen neljällä ja kyseessä on karkausvuosi.
if input / 4 != input // 4:
    print("Jaettuna 4:lle = ", input / 4, "vs",  input // 4)
    print("Jaettuna 100:lle = ", input / 100 , "vs", input // 100)
    print("Jaettuna 400:lle = ", input / 400 , "vs", input // 400)
    print("==================================")
    print("Luvut ei täsmää - Ei karkausvuosi.")

# Onko luku jaollinen 100 mutta ei jaollinen 400?
elif input / 100 == input // 100 and input / 400 != input // 400:
    print("Jaettuna 4:lle = ", input / 4, "vs", input // 4)
    print("Jaettuna 100:lle = ", input / 100, "vs", input // 100)
    print("Jaettuna 400:lle = ", input / 400, "vs", input // 400)
    print("==================================")
    print("Luvut ei täsmää - Ei karkausvuosi.")

# Muussa tapauksessa kyseessä on karkausvuosi
else:
    print("Jaettuna 4:lle = ", input / 4, "vs", input // 4)
    print("Jaettuna 100:lle = ", input / 100, "vs", input // 100)
    print("Jaettuna 400:lle = ", input / 400, "vs", input // 400)
    print("==================================")
    print("Luvut täsmää - Karkausvuosi!")