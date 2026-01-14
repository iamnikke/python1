import math

print("Lasketaan ympyrän pinta-ala.")
radiusInput = int(input("Syötä ympyrän säde senttimetreissä: "))
radius = (radiusInput * 2) * math.pi
print(int(radius), "cm²")