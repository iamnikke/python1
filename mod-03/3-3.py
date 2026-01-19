# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

# ===========================================================================================

print("Selvitä ovatko hemoglobiiniarvosi normaalilla tasolla.")

# .lower() funktio muuntamaan syöte pieniksi kirjaimiksi,
# jotta ohjelma tunnistaa syötteen kirjainkoosta huolimatta; esim käyttäjän syöte mies/Mies/MIES
gender = str(input("Oletko mies vai nainen? ").lower())

# Sukupuolen validointi; mies / nainen / virheviesti
if gender != "mies" and gender != "nainen":
    print("Virheellinen syöte.")
else:
    print("Kiitos! Syötit sukupuoleksesi", gender, ".")
    inputHg = int(input("Syötä hemoglobiiniarvosi (g/l): "))

# Oletusarvot muuttujina. Helppo muokata tarvittaessa suoraan tästä.
femaleDefaultHgMin = 117
femaleDefaultHgMax = 175
maleDefaultHgMin = 134
maleDefaultHgMax = 195

if gender == "mies":
    if inputHg < maleDefaultHgMin:
        print("Matala hemoglobiinitaso!")
    elif inputHg > maleDefaultHgMax:
        print("Korkea hemoglobiinitaso!")
    else:
        print("Normaali hemoglobiinitaso!")

elif gender == "nainen":
    if inputHg < femaleDefaultHgMin:
        print("Matala hemoglobiinitaso!")
    elif inputHg > femaleDefaultHgMax:
        print("Korkea hemoglobiinitaso!")
    else:
        print("Matala hemoglobiinitaso!")
