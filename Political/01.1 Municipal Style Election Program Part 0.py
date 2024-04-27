#Imports stuff
import random
import numpy
import datetime
import matplotlib.pyplot as plt
#Defines variables
regionNumber = 0
CandidatureName = []
TotalPartySeatNumber = []
TotalVotes = []
BaseLikeliness = []
RandomNumber = []
Likeliness = []
listofparty = []
Victories = []
#Asks stuff about the country
Write = input("Do you want to record the results in a file? ")
NumberOfPlaces = "0"
while NumberOfPlaces != int(NumberOfPlaces):
    NumberOfPlaces = int(input("How many number of places are going through local election? "))
with open('CountryDataMunicipal.txt', 'r+') as CountryData:
    for AddLines in range(NumberOfPlaces):
        CountryData.write('\n')
with open('CountryDataMunicipal.txt', 'r+') as CountryData:
    lines = CountryData.readlines()
PartyNumber = "0"
while PartyNumber != int(PartyNumber):
    PartyNumber = int(input("How many parties are there? "))
PartyNumber = PartyNumber+1
Chart = "yes"
Write = Write.lower()
if Write == "yes":
    print("Wiriting.")
    File = open("Results.txt","a")
CountryName = input("What is the name of the country/region? ")
for listofparties in range(PartyNumber):
    listofparty.append(listofparties)
for listofseats in range(PartyNumber):
    TotalPartySeatNumber.append(0)
for listofvotes in range(PartyNumber):
    TotalVotes.append(0)
if Write == "yes":
    DateElection= datetime.datetime.now()
    File.write("\n")
    File.write("\n")
    File.write("\n")
    File.write("#############################################################################")
    File.write("Elections for the "+CountryName+ " parliament on the "+str(DateElection)+"\n")
for CanName in range(PartyNumber-1):
    NewName= input("Who is candidate {}? Please do this with the smallest parties at the end. ".format(CanName+1))
    CandidatureName.append(NewName)
CandidatureName.append("Blank Votes")
print("All numbers have to add up to 100.")
for BaseLikely in range(PartyNumber-1):
    ProbabilityAdding = round(float(input("Probability of {} being voted? ".format(CandidatureName[BaseLikely]))) / 100, 7)
    BaseLikeliness.append(ProbabilityAdding)
BaseLikeliness.append(0)
    #print(BaseLikeliness)
for victoryNum in range(PartyNumber):
    Victories.append(0)
for IdoNotRemember in range(NumberOfPlaces):
    print()
    regionName = str(IdoNotRemember+1)
    notP = random.random()
    if notP < 0.70:
        RegionCountryPop = random.randint(1,5000)
    elif notP >= 0.70 and notP <0.85:
        RegionCountryPop = random.randint(5001,10000)
    elif notP >= 0.85 and notP <0.93:
        RegionCountryPop = random.randint(10001,20000)
    elif notP >= 0.93 and notP <0.981:
        RegionCountryPop = random.randint(20001,50000)
    else:
        RegionCountryPop = random.randint(50001,500000)
    if RegionCountryPop < 100:
        SeatNumber = 3
    elif RegionCountryPop >= 100 and RegionCountryPop <=250:
        SeatNumber = 5
    elif RegionCountryPop >= 251 and RegionCountryPop <=1000:
        SeatNumber = 7
    elif RegionCountryPop >= 1001 and RegionCountryPop <=2000:
        SeatNumber = 9
    elif RegionCountryPop >= 2001 and RegionCountryPop <=5000:
        SeatNumber = 11
    elif RegionCountryPop >= 5001 and RegionCountryPop <=10000:
        SeatNumber = 13
    elif RegionCountryPop >= 10001 and RegionCountryPop <=20000:
        SeatNumber = 17
    elif RegionCountryPop >= 20001 and RegionCountryPop <=50000:
        SeatNumber = 21
    elif RegionCountryPop >= 50001 and RegionCountryPop <=100000:
        SeatNumber = 25
    elif RegionCountryPop >= 100001:
        SeatNumber = 25 + int(round(RegionCountryPop/100000,0))
        if SeatNumber % 2 == 0:
            SeatNumber = SeatNumber+1
        else:
            SeatNumber = SeatNumber
    if Write == "yes":
        File.write("Names:"+"\n")
        File.writelines(CandidatureName)
        File.write("Number of regions: "+str(NumberOfPlaces)+ " Total Original Population: "+str(RegionCountryPop)+" Number of Seats: "+str(SeatNumber)+"\n")
    #Sets variables to 0
    NewCountryPop = int(0)
    SomethingPartyNumber = 0
    for SomethingPartyNumber in range(PartyNumber):
        TotalPartySeatNumber.append(0)
    #Main bulk of the program
    regionNumber =0
    for regionNumber in range(int(1)):
    #Asks stuff about the region and candidatures, as well as sets stuff to 0
        RegionalVotes = []
        votingI = 0
        for votingI in range(PartyNumber):
            RegionalVotes.append(0)
        RegionalSeats = []
        votingseats = 0
        for votingseats in range(PartyNumber):
            RegionalSeats.append(0)
        i=int(0)
        population = RegionCountryPop
        if Write == "yes":
            File.write("Name of region: "+str(regionName) +" Original population: "+str(population)+"\n")
        ListSet = "normal"
        #Cheats = input("HI :) ")
    #Calculates the amounts of seats for the region
        regionSeatsNumber = SeatNumber
        print()
        print()
        print()
        print()
        print()
    #Population changer
        total = int(random.uniform(regionSeatsNumber,population))
        PopMethod = "one"
        participation = round((total/population)*100,2)
        ExtraRandQ = "yes"
        if ExtraRandQ == "yes":
            FactRam = random.uniform(5,6.5)
            if FactRam <= 5.3:
                divValRan = 4
            elif FactRam > 5.3:
                divValRan = 1
        else:
            fekoff = 0 
    #Picks a list from the default ones
        if ListSet == "normal":
            candidature = []
            method = "random"
            if method == "random":
                HowManyParties = random.randint(100,180)
            SetLikeliness = []
            SetLike = 0
            for SetLike in range(PartyNumber-1):
                LikeValue = round(random.uniform(BaseLikeliness[SetLike]/2, BaseLikeliness[SetLike]*1.25),7)
                SetLikeliness.append(LikeValue)
            p=0
            for p in range(HowManyParties):
                RealTotal = 0
                while RealTotal !=1:
                    Likeliness = []
                    RandomNumber=[]
                    pte=0
                    randomiser =0 
                    for randomiser in range(PartyNumber-1):
                        if SetLikeliness[randomiser] > 0.15:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/5,(SetLikeliness[randomiser])/5),7)
                        elif SetLikeliness[randomiser] <0.16 and SetLikeliness[randomiser] > 0.10:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/3,(SetLikeliness[randomiser])/3),7)
                        elif SetLikeliness[randomiser] <0.10:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/2,(SetLikeliness[randomiser])/2),7)
                        elif SetLikeliness[randomiser] <0.01:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser]),(SetLikeliness[randomiser])),7)
                        RandomNumber.append(TheRandom)
                        #print(TheRandom)
                    #print(RandomNumber)
                    addernumber =0 
                    for addernumber in range(PartyNumber-1):
                        Likeliness.append(0)
                        Likeliness[addernumber] = round(SetLikeliness[addernumber]+RandomNumber[addernumber],7)
                        #print(Likeliness[addernumber])
                    #print(Likeliness)
                    #input("shatter me")
                    TotalC= 0
                    totalcadd = 0 
                    for totalcadd in range(PartyNumber-1):
                        TotalC = TotalC + Likeliness [totalcadd]
                    #print(TotalC)
                    if TotalC > 1:
                        Diff = round(TotalC - 1,7)
                        if BaseLikeliness[0] >0.2 and BaseLikeliness [1]>0.2:
                            Likeliness[1] = Likeliness[1]-Diff/2
                            Likeliness[0] = Likeliness[0]-Diff/2
                        elif BaseLikeliness[0] > 0.65:
                            Likeliness[0] = Likeliness[0]-Diff
                        pte = 0
                        Likeliness.append(pte)
                        #print(Likeliness)
                        #print("No peep")
                    elif TotalC <= 1:
                        pte = round(1 - TotalC,7)
                        Likeliness.append(pte)
                        #print(Likeliness)
                        #print("Peep")
                    RealTotal = 0
                    RealTotalii = 0
                    for RealTotalii in range(PartyNumber):
                        RealTotal = round(RealTotal + Likeliness[RealTotalii],7)
                    #print(Likeliness)
                    #print(RealTotal)
                    #if RealTotal !=1 or RealTotal > 1:
                        #print("oh crap, well, if you got here, that is not good news")
                        #print(RealTotal)

                #print("I am looking for this",Likeliness)
                #print(candidature)
                #print(Likeliness)
                NewParty = numpy.random.choice(listofparty, p=Likeliness)
                candidature.append(NewParty)
                #print("this is after", candidature)
            if HowManyParties <= 35:
                listofpartiessmall = 0
                candidature.extend(listofparty)
            if ExtraRandQ == "yes":
                c1 = []
                o = 0
                for o in range(int(round(((PartyNumber)*1.5)/divValRan,0))):
                    Opt1 = random.choice(listofparty)
                    c1.append(Opt1)
                oo = 0
                c2 = []
                for oo in range(int(PartyNumber)*3):
                    Opt2 = random.choice(c1)
                    c2.append(Opt2)
                c3 = []
                ooo=0
                for ooo in range(int(round((len(candidature)/float(FactRam)),0))):
                    Opt3 = random.choice(c2)
                    c3.append(Opt3)
                candidature.extend(c3)
            else:
                fekoff=0
            Cheats ="random"
            if Cheats == "random":
                RandomCheat = random.randint(1,20)
            else:
                RandomCheat=0
            if Cheats == "minor" or RandomCheat == 1:
                #print("I hope you are over 18! You know... so you can vote!")
                NewAddition = int(round(((HowManyParties/4)*2), 0))
                for New in range(NewAddition):
                    if len(listofparty) > 6:
                        candidature.append(0)
                        candidature[-1]=random.choice([listofparty[-1],listofparty[-2],listofparty[-3],listofparty[-4]])
                    else:
                        fekoff =0
            elif Cheats == "juanma" or RandomCheat == 2:
                #print("Female Juanma looks like Olona")
                NewAddition = int(round((HowManyParties/2*1), 0))
                Decider = random.randint(1,2)
                if Decider == 1:
                    CheatPartyOption = random.choice([listofparty[0],listofparty[0],listofparty[1]])
                elif not(Decider == 1):
                    CheatPartyOption = random.choice(listofparty)
                for New in range(NewAddition):
                    candidature.append(CheatPartyOption)
            elif Cheats == "bi" or RandomCheat == 3:
                #print("El Bipartidito")
                NewAddition = int(round(((HowManyParties/4)), 0))
                for New in range(NewAddition):
                    candidature.append(0)
                    candidature[-1] = listofparty[0]
                    candidature.append(0)
                    candidature[-1] = listofparty[1]
            elif Cheats == "enforced" or RandomCheat == 4:
                #print("You have to vote, NOW")
                if PopMethod =="one":
                    total = population
            elif Cheats == "extreme" or RandomCheat == 5:
                #print("This is getting extreme...")
                NewAddition = int(round(((HowManyParties/4)*1.5), 0))
                for New in range(NewAddition):
                    if len(candidature) > 8:
                        candidature.append(0)
                        candidature[-1] = candidature[-3]
                        candidature.append(0)
                        candidature[-1] = candidature[-4]
                    else:
                        fekoff =0
            elif RandomCheat >= 6 and RandomCheat <= 18:
                #print("Swinging is fun.")
                CheatPartyOption = random.choice(listofparty)
                Swing = numpy.random.choice([2,5,10,15],p=[0.3,0.35,0.25,0.1])
                TimesToAdd = int(round((len(candidature)*Swing)/100,0))
                AddingParties=0
                for AddingParties in range(TimesToAdd):
                    candidature.append(CheatPartyOption)
            else:
                fekoff = 0
                #print("Kri kri kri kri.")
            #print("Candidature", candidature)
        else:
            fekoff = 0
        #print(candidature,candiNum)
    #Allows next part to be done
        check = 0
    #Here is where it runs the elections
        while check != regionSeatsNumber:
    #Part where the elections are done if there are 2 or more seats
            if regionSeatsNumber >=2:
    #Runs election
                votingnumbersomething = 0
                for votingnumbersomething in range(total):
                    choice = random.choice(candidature)
                    isthisit = 0
                    for isthisit in range(PartyNumber):
                        if choice == listofparty[isthisit]:
                            RegionalVotes[isthisit] = RegionalVotes[isthisit] +1
                            #print(RegionalVotes)
                countingvotes = 0
                for countingvotes in range(PartyNumber):
                    TotalVotes[countingvotes] = TotalVotes[countingvotes] + RegionalVotes[countingvotes]
                #print(RegionalVotes,total)
                ValidCounting = 0
                ValidVotes=0
                for ValidCounting in range(PartyNumber-1):
                    ValidVotes = ValidVotes+RegionalVotes[ValidCounting]
    #Calculates seats for each party
                isthisitseats = 0
                for isthisitseats in range(PartyNumber-1):
                    RegionalSeats[isthisitseats] = round((RegionalVotes[isthisitseats]/ValidVotes)*regionSeatsNumber,0)
                    #print(RegionalSeats)
                check = 0
                chekingsissy = 0
                for chekingsissy in range(PartyNumber):
                    check = check + RegionalSeats[chekingsissy]
                #Checks whether the seats are too high or too low
                Diff = regionSeatsNumber - check
                #print("Check", check, "Rregion seat number",regionSeatsNumber, "Diff", Diff)
    #If the seats are lower than what they should be, a random candidate is given a seat
                if Diff > 0:
                    for bigfaty in range(int(Diff)):
                        RegionalSeats[0] = RegionalSeats[0] +1
                    print("over")
                    break 
    #If the seats are higher than what they should be, the different is turned positive and then a candidate is removed a seat
                elif Diff<0:
                    Diff = Diff*-1
                    for smallfaty in range(int(Diff)):
                        RegionalSeats[0] = RegionalSeats[0] -1
                    print("under")
                    break
    #If the seats are what they should be, this stops the election and gets the results
                elif Diff==0:
                    print("All good!")
                checkingagain = 0
                check2 = 0
                for checkingagain in range(PartyNumber):
                    check2 = check2 + RegionalSeats[checkingagain]
                #print("Check", check2, "Rregion seat number",regionSeatsNumber, "Diff", Diff)
    #Reruns elections because something is not right
                if check2 != regionSeatsNumber:
                    #print(check2, regionSeatsNumber,"this is sayters fault")
                    #input()
                    sayter = 0
                    for sayter in range(PartyNumber):
                        RegionalVotes[sayter] = 0
                    sayter2 = 0
                    for sayter2 in range(PartyNumber):
                        RegionalSeats[sayter2] = 0
    #If the seat amount for the region is only 1, then it checks who got the most votes
            elif regionSeatsNumber == 1:
                OneSeatVote = []
                oneplace = 0
                for oneplace in range(PartyNumber):
                    OneSeatVote.append(0)
                RegionalSeats = []
                onepiece = 0
                for onepiece in range(PartyNumber):
                    RegionalSeats.append(0)
                #Runs the election
                votingnumberone=0
                for votingnumberone in range(total):
                    choice = random.choice(candidature)
                    isthisitpice = 0
                    for isthisitpice in range(PartyNumber):
                        if choice == listofparty[isthisitpice]:
                            RegionalVotes[isthisitpice] = RegionalVotes[isthisitpice] +1
                countingvotesone = 0
                for countingvotesone in range(PartyNumber):
                    TotalVotes[countingvotes] = TotalVotes[countingvotes] + RegionalVotes[countingvotes]
    #Checks who got most
                CopyingTableT = []
                CopyingTableTID = 0
                for CopyingTableTID in range(PartyNumber-1):
                    CopyingTableT.append(RegionalVotes[CopyingTableTID])
                MaxCand = CopyingTableT.index(max(CopyingTableT))
                #print(MaxCand)
                RegionalSeats[MaxCand] = 1
                print("Party",CandidatureName[MaxCand],"got the seat.")
                check = 0
                chekingone = 0
                for chekingone in range(PartyNumber):
                    check = check + RegionalSeats[chekingone]
                #print("checl",check,"regional",regionSeatsNumber)
    #Prints the results for the region
        print("For region", regionName," the results were:")
        print("Seats to asign:",regionSeatsNumber)
        print("Number of entries", total)
        pringtingregional = 0
        for pringtingregional in range(PartyNumber):
            print(CandidatureName[pringtingregional]," got ", RegionalVotes[pringtingregional], " and ", RegionalSeats[pringtingregional]," seats.")
        print("Participation was", participation, "%.")
        CopyingTableO = []
        CopyingTableOID = 0
        for CopyingTableOID in range(PartyNumber-1):
            CopyingTableO.append(RegionalVotes[CopyingTableOID])
        WinnerRegional = CopyingTableO.index(max(CopyingTableO))
        print(CandidatureName[WinnerRegional],"is the winner of the region.")
        Victories[WinnerRegional] = Victories [WinnerRegional] +1
        if Write == "yes":
            File.write("For region "+ str(regionName)+" the results were:"+"\n")
            File.write("Seats to asign: "+str(regionSeatsNumber)+"\n")
            File.write("Number of entries "+ str(total)+"\n")
            for pringtingregional in range(PartyNumber):
                File.write(str(CandidatureName[pringtingregional])+" got "+ str(RegionalVotes[pringtingregional])+ " and "+ str(RegionalSeats[pringtingregional])+" seats."+"\n")
            File.write("Participation was "+ str(participation)+ "%."+"\n")
            File.write(str(CandidatureName[WinnerRegional])+" is the winner of the region.")
    #Pie for region
        #if Chart == "yes":
        # plt.pie(RegionalVotes,labels = CandidatureName)
        # plt.title("Votes per Party")
        # plt.show()
        addingupseats = 0
        for addingupseats in range(PartyNumber):
            TotalPartySeatNumber[addingupseats] = TotalPartySeatNumber[addingupseats] + RegionalSeats [addingupseats]
        print()
        print()
        print()
        print()
        print()
        lines[IdoNotRemember] = f'"{regionName}",{population}\n'
#Prints the results for the whole place
with open('CountryDataMunicipal.txt', 'w') as CountryData:
    CountryData.writelines(lines)
for finalprint in range(PartyNumber):
    print("Total seats for ",CandidatureName[finalprint], " are ",TotalPartySeatNumber[finalprint],". Total votes are",TotalVotes[finalprint],". Number of victories are", Victories[finalprint],".")
TotalSeats = 0
for anotherone in range(PartyNumber):
    TotalSeats = TotalSeats + TotalPartySeatNumber[anotherone]
TotalVotesGeneral = 0
for TotalVotesCount in range(PartyNumber):
    TotalVotesGeneral = TotalVotesGeneral + TotalVotes[TotalVotesCount]
print("The number of seats asigned",TotalSeats,". And total entries",TotalVotesGeneral)
WinnerTotal = TotalPartySeatNumber.index(max(TotalPartySeatNumber))
print(CandidatureName[WinnerTotal],"is the winner of the election!")
#Graph stuff
if Chart == "yes":
    graphvalue=[]
    notagain=0
    for notagain in range(PartyNumber):
        graphvalue.append(TotalPartySeatNumber[notagain])
    plt.bar(CandidatureName,graphvalue)
    plt.xlabel("Party")
    plt.ylabel("Number of Seats")
    plt.title("Election Results")
    plt.show()
#Final writting
if Write == "yes":
    File.write("\n")
    for finalwrite in range(PartyNumber):
        File.write("Total seats for "+str(CandidatureName[finalwrite])+ " are "+str(TotalPartySeatNumber[finalwrite])+". And votes are "+str(TotalVotes[finalwrite])+".")
    File.write("The number of seats asigned "+str(TotalSeats)+"."+"\n")
    File.write(str(CandidatureName[WinnerTotal])+"is the winner of the election!")
    File.write("#############################################################################")
    File.close()
input()