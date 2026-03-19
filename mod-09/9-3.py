"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

    def travel(self, hours):
        distanceTraveled = hours * self.currentSpeed
        self.totalDistance += distanceTraveled
        print(f"Matkaa tuli {distanceTraveled} km")
        print(f"Olet nyt matkustanut yhteensä {self.totalDistance} km")




car = Car("ABC-123", 142)

print(f"Auton rekisteritunnus on {car.license}")
print(f"Auton huippunopeus on {car.maxSpeed} km/h")
print(f"Auton nykyinen nopeus on {car.currentSpeed} km/h")
print(f"Auto on matkustanut yhteensä {car.totalDistance} km")

car.accelerate(30)
car.travel(1.5)
car.accelerate(70)
car.travel(1.5)
car.accelerate(50)
car.travel(1.5)
car.accelerate(-200)
car.travel(1.5)


