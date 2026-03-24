"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai
kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä
yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet
pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

"""

class Elevator:

    def __init__(self):
        self.minFloor = 1
        self.maxFloor = 6
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


hiss = Elevator()

print("> Olet kerroksessa", hiss.currentFloor)
hiss.moveToFloor(5)

print("")

print("> Olet kerroksessa", hiss.currentFloor)
hiss.moveToFloor(2)

print("")

print("> Olet kerroksessa", hiss.currentFloor)
hiss.moveToFloor(10)


