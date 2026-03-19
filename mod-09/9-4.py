"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

"""
import random

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
#        if speed < 0:
#            print(f"Auto ({self.license}) jarruttaa {speed} km/h joten nykyinen nopeus on {self.currentSpeed} km/h")
#        else:
#            print(f"Auto ({self.license}) kiihdyttää {speed} km/h joten nykyinen nopeus on {self.currentSpeed} km/h")

    def travel(self, hours):
        distanceTraveled = hours * self.currentSpeed
        self.totalDistance += distanceTraveled
        return distanceTraveled
#        print(f"Matkaa tuli {distanceTraveled} km")
#        print(f"Olet nyt matkustanut yhteensä {self.totalDistance} km")




carsList = []

for i in range(1,11):

    licensePlate = "ABC" + str(i)
    maxSpeed = random.randint(100,200)

    car = Car(licensePlate, maxSpeed)
    carsList.append(car)

for car in carsList:
    print(f"{car.license} - {car.maxSpeed} km/h")





print("Autot luotu")
print("Kilpailu alkaa!")
print("")


race = True

while race:

    for car in carsList:

        accelerationAmount = random.randint(-10, 15)
        car.accelerate(accelerationAmount)
        travelAmount = car.travel(1)

        print(f"{car.license} ||| {car.totalDistance}km ({travelAmount}) ||| {car.maxSpeed}km/h ||| {car.currentSpeed}km/h ({accelerationAmount}) | ")

        if car.totalDistance >= 10000:

            print("")
            print("KISA OHI - TULOKSET")
            print("REK. NRO ||| KULJETTU MATKA ||| HUIPPUNOPEUS ||| NYKYINEN NOPEUS |")
            for car in carsList:
                print(f"{car.license}     |||     {car.totalDistance}km     |||    {car.maxSpeed}km/h    |||     {car.currentSpeed}km/h    | ")

            # Riko while-loop
            race = False
            # Riko for-loop
            break



