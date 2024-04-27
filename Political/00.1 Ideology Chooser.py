import random
NumbSets= int(input("How many sets do you want? "))
ocracy_dict = {
    "Democracy": ["Demarchy", "Census democracy", "Direct democracy", "Electocracy", "Herrenvolk democracy", "Liberal democracy", "Liquid democracy", "Representative democracy", "Social democracy", "Soviet democracy", "Totalitarian democracy", "Electoral autocracy", "Digital democracy"],
    "Oligarchy": ["Aristocracy", "Ergatocracy", "Geniocracy", "Hamarchy", "Kraterocracy", "Kritarchy", "Meritocracy", "Netocracy", "Noocracy", "Plutocracy", "Particracy", "Stratocracy", "Synarchism", "Technocracy", "Theocracy", "Timocracy"],
    "Autocracy": ["Civilian dictatorship", "Military dictatorship"]
}

power_dict = {
    "Monarchy": ["Absolute monarchy", "Constitutional monarchy", "Crowned republic", "Elective monarchy"],
    "Republic": ["Classical republic", "Constitutional republic", "Democratic republic", "Federal republic", "Religious republic", "Parliamentary republic", "Presidential republic", "People's republic", "Semi-presidential republic", "Directorial republic", "Merchant republic"]
}

SocioEconomic = ["Anarchism","Capitalism","Colonialism","Communism","Despotism","Distributism","Feudalism","Minarchism","Monarchism","Republicanism","Socialism","Totalitarianism","Tribalism"]

for i in range(NumbSets):
    random_ocracy = random.choice(list(ocracy_dict.keys()))
    ocracy_picked = random.choice(ocracy_dict[random_ocracy])
        
    power_choose = random.choice(list(power_dict.keys()))
    power_picked = random.choice(power_dict[power_choose])
    SocioPicked = random.choice(SocioEconomic)
    print("")
    print(f"Values for Party {i+1}:")
    print(f"Type of ocract: {ocracy_picked}")
    print(f"Type of power: {power_picked}")
    print(f"Type of social-economic main policy: {SocioPicked}")