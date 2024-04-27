import random
import math
NameStar = input("What is the name of the star? ")
PlanetNumber = int(input("How many planetary bodies are there? "))
#actual rocks or venusian
rockyHot = ["Volcanic Plains", "Lava Fields", "Asteroid Craters", "Volcanic Moon", "Barren", "Desert", "Mountainous", "Proto World", "Shadow Proto World", "Wasteland", "Dark Red Desert", "Red Desert", "Sulphuric", "Tar Ball", "Scorched", "Volcanic"]
rockyCold = ["Lunar", "Rocky Moon", "Desert Moon", "Toxic Moon","Frozen Moon"]
rocky = ["Aether", "Sulphuric", "Gelatinous", "Chromatic", "Unknown"]
EarthLikeColdOcean = ["Polar Ice Caps","Tundra","Kelp Forests (ocean floor)","Ice Waste","Dark Ice Waste","Arctic","Dark Arctic"]
EarthLikeCold = ["Ice Plains","Glacier","Permafrost Tundra","Snowy","Frozen Volcanic","Irradiated","Tundra","Boreal Forest/Taiga"]
EarthLikeTemperateOcean = ["Temperate Rainforest","Strange Sea","Coral Reefs (ocean floor)","Kelp Forests (ocean floor)","Oceanic","Tidewater"]
EarthLikeTemperate = ["Plains/lush/garden","Cold Desert","Temperate seasonal forest","Temperate Deciduous Forests","Primeval Forest","Fungal","Eden","Alien","Grasslands","Shrublands","Temperate Forests","Jungle","Mountainous"]
EarthLikeHotOcean = ["Tropical Rainforests","Mangrove Swamps", "Wetland", "Oceanic"]
EarthLikeHot = ["Hot Deserts", "Sand Dunes", "Rock Deserts","Jungle", "Savanna", "Wasteland"]
GasGiant = ["Proto Giant","Ammonia Clouds", "Metallic Hydrogen Core", "Storm", "Flame Giant", "Ice Giant", "Gas Giant (Ice)", "Gas Giant (Hot)", "Super Dense", "Toxic Giant"]
MicroBiomes = ["Alien Forest","Alien Desert","Ancient Glade","Apple Orchard","Ash Garden","Badlands","Bamboo Forest","Banana Forest","Birch Forest","Black Slime Bog","Blister Bush Field","Blood Gulch","Bloodstone Woods","Bracken Field","Breakwater","Cactus Place","Caliche Vein","Coniferous Forest","Carrot Crop","Colorful Desert Oasis","Cornfield","Cellular Expanse","Cloud Forest","Clouds","Corrupt","Crystalline Swamp","Crystalline Desert","Crystalline Volcanic","Dark Zone","Deadwood","Deep Sea Vent","Dry Riverbed","Eldritch Field","Eldritch Forest","Estuary","Flower Forest","Erchius Crystal Expanse","Glacial","Gore Forest","Haunted Forest","Haunted Graveyard","Hellfire Field","Hell Hive","Hive","Hot Springs","Icefire Forest","Irradiated Glade","Kelp Forest","Magic Snow Land","Meadow","Metal Hive","Metal Jungle","Parking Lot","Peach Orchard","Pear Orchard","Potato Field","Rainbow Wood (biome)","Red Wastes","Reef","Rusted Hulk","Tentacle Asteroids","Sugarcane Field","Volcanic Sulphuric","Sulphur Pits","Taiga","Tar Pits","Tomato Garden","Unsalvaged Hulk","Vineyard","Wheat Field","Winter Glade"]
EarthLikeColdTotal =[]
EarthLikeColdTotal.extend(EarthLikeColdOcean)
EarthLikeColdTotal.extend(EarthLikeCold)
EarthLikeTemperateTotal =[]
EarthLikeTemperateTotal.extend(EarthLikeTemperate)
EarthLikeTemperateTotal.extend(EarthLikeTemperateOcean)
EarthLikeHotTotal =[]
EarthLikeHotTotal.extend(EarthLikeHotOcean)
EarthLikeHotTotal.extend(EarthLikeHot)
for PlanetCounter in(range(PlanetNumber)):
    BiomesToPickFrom = []
    BiomesPickedList = []
    MicroBiomesPickedList = []
    ColdCheck = False
    TemperateCheck = False
    HotCheck =  False
    PlanetType = input("What type of planet is it? ")
    LowTemp = float(input("What is the minimum temperature? "))
    HighTemp = float(input("What is the maximum temperature? "))
    Radius = int(input("In kilometres, what is the radius of the object? "))
    OceanAsk = input("Does the planet have an ocean? ")

    SurfaceArea = 4*math.pi*Radius**2
    NumberOfBiomes = int(round(math.log(SurfaceArea),0))
    if NumberOfBiomes == 0:
        NumberOfBiomes = 1


    if PlanetType == "rocky":
        BiomesToPickFrom.extend(rocky)
        if LowTemp < -10 or HighTemp<0:
            BiomesToPickFrom.extend(rockyCold)
        if LowTemp > 50 or HighTemp>50:
            BiomesToPickFrom.extend(rockyHot)
    elif PlanetType == "venusian":
        BiomesToPickFrom.extend(rockyHot)
        BiomesToPickFrom.append("Sulphuric ocean")
    elif PlanetType == "gas giant":
        BiomesToPickFrom.extend(GasGiant)
    elif PlanetType == "earth-like":
        TotalTempRange = HighTemp-LowTemp
        if LowTemp > 0:
            BelowZPer = 0
        elif LowTemp < 0:
            BelowZ = -1*LowTemp
            BelowZPer = BelowZ/TotalTempRange
        if HighTemp >= 20 or LowTemp >= 20:
            if LowTemp >=20:
                AboveTwentyPer=1
            elif LowTemp <20:
                AboveTwenty = HighTemp-20
                AboveTwentyPer = AboveTwenty/TotalTempRange
        elif HighTemp < 20:
            AboveTwentyPer = 0
        MidTempPer = 1-AboveTwentyPer-BelowZPer

        for coldbiome in range(int(round(NumberOfBiomes*2*BelowZPer,0))):
            if OceanAsk == "yes":
                BiomesToPickFrom.append(random.choice(EarthLikeColdTotal))
            else:
                BiomesToPickFrom.append(random.choice(EarthLikeCold))
        for temperatebiome in range(int(round(NumberOfBiomes*2*MidTempPer,0))):
            if OceanAsk == "yes":
                BiomesToPickFrom.append(random.choice(EarthLikeTemperateTotal))
            else:
                BiomesToPickFrom.append(random.choice(EarthLikeTemperate))
        for hotbiome in range(int(round(NumberOfBiomes*2*AboveTwentyPer,0))):
            if OceanAsk == "yes":
                BiomesToPickFrom.append(random.choice(EarthLikeHotTotal))
            else:
                BiomesToPickFrom.append(random.choice(EarthLikeHot))
    BiomeCounter = 0
    if OceanAsk == "yes":
        NumberOfBiomes =NumberOfBiomes+5
    for BiomeCounter in(range(NumberOfBiomes)):
        PickedBiome = random.choice(BiomesToPickFrom)
        BiomesPickedList.append(PickedBiome)
    for MicroBiomeCounter in(range(int(round(NumberOfBiomes/3,0)))):
        PickedMicroBiome = random.choice(MicroBiomes)
        MicroBiomesPickedList.append(PickedMicroBiome)
    print(f"The picked biomes for the planetary body number {PlanetCounter+1} are {', '.join(BiomesPickedList)}.")
    print(f"The picked microbiomes for the planetary body number {PlanetCounter+1} are {', '.join(MicroBiomesPickedList)}.")