"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

"""

class Car:
    def __init__(self, license, maxSpeed):
        self.license = license
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0
        self.totalDistance = 0

    def accelerate(self, speed):

        self.currentSpeed += speed

        # Jos jarrutus hidastaa nopeuden miinus merkkiseksi niin korjataan nopeus nollaan.
        if self.currentSpeed < 0:
            self.currentSpeed = 0

        # Jos kiihdytys on miinusmerkkinen = eli ajoneuvo jarruttaa, niin tehdään toisenlainen tuloste
        if speed < 0:
            print(f"Auto jarruttaa {speed} km/h joten nykyinen nopeus on {self.currentSpeed} km/h")
        else:
            print(f"Auto kiihdyttää {speed} km/h joten nykyinen nopeus on {self.currentSpeed} km/h")




car = Car("ABC-123", 142)

print(f"Auton rekisteritunnus on {car.license}")
print(f"Auton huippunopeus on {car.maxSpeed} km/h")
print(f"Auton nykyinen nopeus on {car.currentSpeed} km/h")
print(f"Auto on matkustanut yhteensä {car.totalDistance} km")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.accelerate(-200)

