class Car:
    def __init__(self, license, maxSpeed):
        self.license = license
        self.maxSpeed = maxSpeed
        self.currentSpeed = 0
        self.totalDistance = 0

    def accelerate(self, speedChange):
        self.currentSpeed += speedChange

        if self.currentSpeed < 0:
            self.currentSpeed = 0
        elif self.currentSpeed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed

    def travel(self, hours):
        self.totalDistance += self.currentSpeed * hours


class ElectricCar(Car):
    def __init__(self, license, maxSpeed, batteryCapacity):
        super().__init__(license, maxSpeed)
        self.batteryCapacity = batteryCapacity


class GasCar(Car):
    def __init__(self, license, maxSpeed, tankSize):
        super().__init__(license, maxSpeed)
        self.tankSize = tankSize


# Main program

electricCar = ElectricCar("ABC-15", 180, 52.5)
gasCar = GasCar("ACD-123", 165, 32.3)

electricCar.accelerate(120)
gasCar.accelerate(100)

electricCar.travel(3)
gasCar.travel(3)

print(f"Electric car {electricCar.license}, distance: {electricCar.totalDistance} km")
print(f"Gas car {gasCar.license}, distance: {gasCar.totalDistance} km")