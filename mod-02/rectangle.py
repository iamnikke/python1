import math

print("Lasketaan suorakulmion piiri ja pinta-ala.")
height = int(input("Syötä ympyrän säde senttimetreissä: "))
width = int(input("Syötä ympyrän säde senttimetreissä: "))

pintaala = width * height
piiri = 2*(width * height)

print(pintaala)
print(piiri)