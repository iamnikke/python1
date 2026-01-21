# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

inches = int(input("Syötä tuumamäärä: "))
centimeters = inches * 2.54
print(centimeters, "cm")

while inches >= 0:
    inches = int(input("Syötä tuumamäärä: "))
    centimeters = inches * 2.54
    print(centimeters, "cm")
else:
    print("Syötit negatiivisen tuumamäärän!")