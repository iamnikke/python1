"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

"""

class Elevator:

    def __init__(self, minFloor, maxFloor):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.currentFloor = 1

    def floorUp(self):
        newFloor = self.currentFloor + 1

        if newFloor > self.maxFloor:
            newFloor = self.maxFloor

        self.currentFloor = newFloor
        print(f"     - Saavuit kerrokseen {self.currentFloor}")

    def floorDown(self):
        newFloor = self.currentFloor - 1

        if newFloor < self.minFloor:
            newFloor = self.minFloor

        self.currentFloor = newFloor
        print(f"     - Saavuit kerrokseen {self.currentFloor}")

    def moveToFloor(self, newFloor):

        if newFloor > self.maxFloor:
            print(f"VIRHE: Syöttämäsi kerros menee katosta läpi. Korkein sallittu kerros on {self.maxFloor}. Mennään sinne...")
            newFloor = self.maxFloor
        elif newFloor < self.minFloor:
            print(f"VIRHE: Syöttämäsi kerros menee pohjasta läpi. Alin sallittu kerros on {self.minFloor}. Mennään sinne...")
            newFloor = self.minFloor

        print(f"> Siirrytään kerrokseen {newFloor}")

        if newFloor > self.currentFloor:
            for i in range (self.currentFloor, newFloor):
                self.floorUp()
        elif newFloor < self.currentFloor:
            for i in range (newFloor, self.currentFloor):
                self.floorDown()

class House:

    def __init__(self, maxFloor, minFloor, elevatorAmount):
        self.maxFloor = maxFloor
        self.minFloor = minFloor
        self.elevatorAmount = elevatorAmount

        self.elevators = []
        for i in range(elevatorAmount):
            self.elevators.append(Elevator(minFloor, maxFloor))

    def driveElevator(self, elevatorId, targetFloor):

        if elevatorId < 0 or elevatorId >= self.elevatorAmount:
            print("Virhe")
            return

        elevator = self.elevators[elevatorId]
        elevator.moveToFloor(targetFloor)


house = House(5, 5, 10)
house.driveElevator(0, 5)
house.driveElevator(1, 3)
house.driveElevator(2, 10)


