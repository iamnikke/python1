import math

print("Lasketaan suorakulmion piiri ja pinta-ala.")
height = float(input("Syötä korkeus senttimetreissä: "))
width = float(input("Syötä kanta, eli leveys senttimetreissä: "))

pintaala = width * height
piiri = 2 * width + 2 * height

print(pintaala, "cm²")
print(piiri)