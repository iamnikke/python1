print("Lasketaan lukujen summa, tulo ja keskiarvo.")
x = int(input("Syötä leivisköjen määrä: "))
y = int(input("Syötä naulojen määrä: "))
z = int(input("Syötä luotien määrä: "))

# Luodit
zDefault = 13.3
# Neulat
yDefault = 32 * zDefault
# Leiviskät
xDefault = 20 * yDefault

zResult = z * zDefault
yResult = y * yDefault
xResult = x * xDefault

# kokonaismassan yhteenlasku.
totalResult = xResult + yResult + zResult
# konversio kilogrammoiksi, jaetaan tuhannella.
totalResultKilograms = totalResult / 1000

print(totalResultKilograms, " kilogrammaa.")