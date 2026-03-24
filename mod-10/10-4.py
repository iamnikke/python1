import random


class Car:
    def __init__(self, license, maxSpeed):
        self.license = license
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0
        self.totalDistance = 0

    def accelerate(self, speed):
        self.currentSpeed += speed

        if self.currentSpeed < 0:
            self.currentSpeed = 0

        if self.currentSpeed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed

    def travel(self, hours):
        distanceTraveled = hours * self.currentSpeed
        self.totalDistance += distanceTraveled


class Race:
    def __init__(self, name, lengthKm, participants):
        self.name = name
        self.lengthKm = lengthKm
        self.participants = participants

    def tunti_kuluu(self):
        for car in self.participants:
            accelerationAmount = random.randint(-10, 15)
            car.accelerate(accelerationAmount)
            car.travel(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.name}")
        print(f"{'Rek.nro':<10} {'Huippunopeus':<15} {'Nykyinen nopeus':<18} {'Kuljettu matka':<15}")
        print("-" * 60)

        for car in self.participants:
            print(f"{car.license:<10} {car.maxSpeed:<15} {car.currentSpeed:<18} {car.totalDistance:<15}")

    def kilpailu_ohi(self):
        for car in self.participants:
            if car.totalDistance >= self.lengthKm:
                return True
        return False


# Pääohjelma

carsList = []

for i in range(1, 11):
    licensePlate = f"ABC-{i}"
    maxSpeed = random.randint(100, 200)

    car = Car(licensePlate, maxSpeed)
    carsList.append(car)

race = Race("Suuri romuralli", 8000, carsList)

hours = 0

while not race.kilpailu_ohi():
    race.tunti_kuluu()
    hours += 1

    if hours % 10 == 0:
        print(f"\nTilanne {hours} tunnin jälkeen:")
        race.tulosta_tilanne()

print(f"\nKilpailu päättyi {hours} tunnin jälkeen.")
race.tulosta_tilanne()