import math

print("Lasketaan ensin ympyrän pinta-ala.")
radiusInput = float(input("Syötä ympyrän säde senttimetreissä: "))
radius = (radiusInput * 2) * math.pi
print(float(radius), "cm²")
