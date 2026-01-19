# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
# alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

print("Minkä hyttiluokan kuvauksen haluat tietää?")
print("Saatavilla olevat hyttiluokat: LUX / A / B / C")
input = str(input("Kirjoita hyttiluokan tunnus: "))

if input == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif input == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif input == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif input == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

