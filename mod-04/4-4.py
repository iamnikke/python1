# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

guess = int(input("Arvaa numero: "))

answer = random.randint(1, 10)

while guess != answer:
    guess = int(input("Väärin! Arvaa uudestaan: "))

    if guess == answer:
        print("Arvasit", guess, ", joka on...........")
        print("oikea vastaus!")
        break