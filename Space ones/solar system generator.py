import random
PlanetNumber = input("Enter the number of planets, enter r for random: ")
MoonNumber = input("Enter the number of moons, enter r for random: ")
if PlanetNumber == "r":
    PlanetNumber = random.randint(1,20)
else:
    PlanetNumber = int(PlanetNumber)
if MoonNumber == "r":
    MoonNumber = random.randint(1,45)
else:
    MoonNumber = int(MoonNumber)
AUValue = random.uniform(0.1,0.8)
PlanetType =["rock","terrestrial","gas"]
for PlanetCounter in range(PlanetNumber):
    PlanetCounter = PlanetCounter+1
    ChosenType = random.choice(PlanetType)
    MoonLocationKM = 0
    PreviousMoonLocation = 0
    MoonCounter = 0
    if ChosenType == "rock":
        Radius = random.randint(300, 3000)
    elif ChosenType == "terrestrial":
        Radius = random.randint(800, 18000)
    elif ChosenType == "gas":
        Radius = random.randint(25000, 100000)
    print(f"Planet {PlanetCounter} is of type {ChosenType} and is located at {round(AUValue,4)} AU value.")
    if PlanetCounter == PlanetNumber:
        NumberMoons = MoonNumber
    else:
        NumberMoons = random.randint(0,round(MoonNumber/1.5,0))
    for MoonCounter in range(NumberMoons):
        MoonLocationKM = round((random.randint(Radius*4,Radius*30)),5)+PreviousMoonLocation
        print(f"Moon number {MoonCounter+1} for planet {PlanetCounter+1} is located at {MoonLocationKM} KM, which is {round(MoonLocationKM/149597870.7,5)} AU, from its planet.")
        PreviousMoonLocation = round(MoonLocationKM/100,0)
    MoonNumber = MoonNumber - NumberMoons
    AUValue = random.uniform(AUValue*1.2, AUValue*3)

