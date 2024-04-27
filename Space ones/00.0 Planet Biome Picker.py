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
        if LowTemp < 0:
            BiomesToPickFrom.extend(EarthLikeCold)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeColdOcean)
            ColdCheck = True
        elif LowTemp >= 0 and LowTemp < 20:
            BiomesToPickFrom.extend(EarthLikeTemperate)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeTemperateOcean)
            TemperateCheck = True
        elif LowTemp >= 20:
            BiomesToPickFrom.extend(EarthLikeHot)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeHotOcean)
            HotCheck = True
        ####
        if HighTemp < 0 and ColdCheck == False:
            BiomesToPickFrom.extend(EarthLikeCold)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeColdOcean)
            ColdCheck = True
        elif HighTemp >= 0 and HighTemp < 20 and TemperateCheck == False:
            BiomesToPickFrom.extend(EarthLikeTemperate)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeTemperateOcean)
            TemperateCheck = True
        elif HighTemp >= 20 and HotCheck == False:
            BiomesToPickFrom.extend(EarthLikeHot)
            if OceanAsk == "yes":
                BiomesToPickFrom.extend(EarthLikeHotOcean)
            HotCheck = True 
    SurfaceArea = 4*math.pi*Radius**2
    NumberOfBiomes = int(round(math.log(SurfaceArea),0))
    if NumberOfBiomes == 0:
        NumberOfBiomes = 1
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