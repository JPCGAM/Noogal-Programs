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
BaseLikelinessOriginal = []
RandomNumber = []
Likeliness = []
listofparty = []
Victories = []
NewCountryPop =0 
#Asks stuff about the country
with open('CountryData.txt', 'r+') as CountryData:
    lines = CountryData.readlines()
Write = input("Do you want to record the results in a file? ")
SeatsMethod = input("What method for the seat number of each region should be used: a) fixed by hand, b) fixed by file, c) proportional, d) municipal ")
SeatAlocationMethod = input("What type of seat alocation method is it: a) proportional, b) D'Hont, c) winner takes all, d) Sainte-Laguë ")
DoItAll = input("Do you want to enter the time since last election and regional party for every region? a) yes b) no ")
ExtraSeatsWinner = input("Do you want the regional winner to get extra seats: a) yes b) no ")
MethodOfVoting = input("What method of voting should be used: a) Single vote b) Ranked vote c) Multiple options ")
if ExtraSeatsWinner =="a" or ExtraSeatsWinner == "yes":
    ExtraSeatsPercentage = float(input("How percentage extra of seats for winner: "))
    ExtraSeatsPercentage = ExtraSeatsPercentage/100
else:
    ExtraSeatsPercentage = 0
if DoItAll == "b":
    Cheats = "r"
    DaysSince = float(input("How many days has it been since the last election? "))
PartyNumber = int(lines[1].split(',')[0])
PartyNumberOriginal = PartyNumber
PartyNumber = PartyNumber+1
Chart = "yes"
Write = Write.lower()
if Write == "yes":
    print("Wiriting.")
    File = open("Results.txt","a")
CountryName = lines[0].split(',')[0].strip('"')
CountryPopulation = float(lines[0].split(',')[1])
TotalSeatsCountry = float(lines[0].split(',')[2])
print(f"Elections for {CountryName}, with {TotalSeatsCountry} seats.")
for listofparties in range(PartyNumber):
    listofparty.append(listofparties)
for listofseats in range(PartyNumber):
    TotalPartySeatNumber.append(0)
for listofvotes in range(PartyNumber):
    TotalVotes.append(0)
for CanName in range(PartyNumber-1):
    NewName= lines[2].split(',')[CanName].strip('\n')
    CandidatureName.append(NewName)
CompleteNameList= lines[2]
if Write == "yes":
    DateElection= datetime.datetime.now()
    File.write("\n")
    File.write("\n")
    File.write("\n")
    File.write("#############################################################################")
    File.write("Elections for the "+CountryName+ " parliament on the "+str(DateElection)+"\n")
    File.write("Names:"+"\n")
    File.writelines(CandidatureName)
    File.write("Number of regions: "+str(len(lines)-4)+ " Total Original Population: "+str(CountryPopulation)+" Number of Seats: "+str(TotalSeatsCountry)+"\n")

CandidatureName.append("Blank Votes")
#######
participationVariable = float(random.random()) #generates random overal participation rate
#######
CompleteProbabilityList = lines[3].strip('\n')
for BaseLikely in range(PartyNumber-1):
    ProbabilityAdding = round(float(lines[3].split(',')[BaseLikely].strip('\n')) / 100, 7)
    BaseLikelinessOriginal.append(ProbabilityAdding)
BaseLikelinessOriginal.append(0)
    #print(BaseLikeliness)
for victoryNum in range(PartyNumber):
    Victories.append(0)
for IdoNotRemember in range(len(lines)-4):
    print()
    regionName, population = lines[IdoNotRemember+4].strip().split(',')[:2]
    regionName = regionName.strip('"')
    if SeatsMethod == "a":
        regionSeatsNumber = float(input(f"What is the number of seats for region {regionName}: "))
    elif SeatsMethod =="b":
        regionSeatsNumber = float(lines[IdoNotRemember+4].split(',')[2])
    elif SeatsMethod == "c":
        regionSeatsNumber = round((float(population)/CountryPopulation)*TotalSeatsCountry,0)
    elif SeatsMethod == "d":
        population = float(population)
        if population < 100:
            SeatNumber = 3
        elif population >= 100 and population <=250:
            SeatNumber = 5
        elif population >= 251 and population <=1000:
            SeatNumber = 7
        elif population >= 1001 and population <=2000:
            SeatNumber = 9
        elif population >= 2001 and population <=5000:
            SeatNumber = 11
        elif population >= 5001 and population <=10000:
            SeatNumber = 13
        elif population >= 10001 and population <=20000:
            SeatNumber = 17
        elif population >= 20001 and population <=50000:
            SeatNumber = 21
        elif population >= 50001 and population <=100000:
            SeatNumber = 25
        elif population >= 100001:
            SeatNumber = 25 + int(round(population/100000,0))
            if SeatNumber % 2 == 0:
                SeatNumber = SeatNumber+1
            else:
                SeatNumber = SeatNumber
        regionSeatsNumber = SeatNumber
    
    print(f"For region {regionName}:")
    if DoItAll == "a":
        AskRegional = int(input("How many regional parties are there? If none, enter 0. This can also be used to lower the value of national parties if revelant. "))
    elif DoItAll =="b":
        CheckRegionalParties = int(lines[IdoNotRemember+4].split(',')[3])
        if CheckRegionalParties == 0:
            AskRegional = 0
        else:
            AskRegional = CheckRegionalParties
    BaseLikeliness = BaseLikelinessOriginal.copy()
    if AskRegional == 0:
        BaseLikeliness = BaseLikelinessOriginal.copy()
    elif AskRegional != 0 and DoItAll =="a":
        PartiesIDRegionalAmount = []
        PartyVoteRegionalAmount=[]
        RegionalPartyChangerCounter = 0
        BaseLikeliness = BaseLikelinessOriginal.copy()
        for RegionalPartyChangerCounter in range(int(AskRegional)):
            PartyIDChange = int(input("Which is the candidate number for the regional party? "))
            PartyIDChange = PartyIDChange-1
            PartiesIDRegionalAmount.append(PartyIDChange)
            PartyRegionalChange = round(float(input("Probability of {} being voted in the region? ".format(CandidatureName[PartyIDChange])))/ 100, 7)
            BaseLikeliness[PartyIDChange]=PartyRegionalChange
            PartyVoteRegionalAmount.append(PartyRegionalChange*100)
    elif AskRegional != 0 and DoItAll =="b":
        PartiesIDRegionalAmount = []
        PartyVoteRegionalAmount=[]
        RegionalPartyChangerCounter = 0
        BaseLikeliness = BaseLikelinessOriginal.copy()
        for RegionalPartyChangerCounter in range(int(AskRegional)):
            PartyIDChange =  int(lines[IdoNotRemember+4].split(',')[RegionalPartyChangerCounter+4])
            PartiesIDRegionalAmount.append(PartyIDChange)
            PartyRegionalChange = round(float(lines[IdoNotRemember+4].split(',')[RegionalPartyChangerCounter+4+AskRegional])/100,7)
            BaseLikeliness[PartyIDChange]=PartyRegionalChange
            PartyVoteRegionalAmount.append(PartyRegionalChange*100)

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
        population = float(population)
        if Write == "yes":
            File.write("\n")
            File.write("Name of region: "+str(regionName) +" Original population: "+str(population)+"\n")
        ListSet = "normal"
        #Cheats = input("HI :) ")
    #Calculates the amounts of seats for the region
        if regionSeatsNumber < 1:
            regionSeatsNumber = 1
    #Population changer
        #Participation bit
        #####
        if participationVariable*1.5 > 1:
                participationVariableHigher = 1
        elif participationVariable*1.5 <= 1:
                participationVariableHigher=participationVariable*1.5
        participationVariableFurther = random.uniform((participationVariable/2),participationVariableHigher)
        if DoItAll =="a":
            DaysSince = float(input("How many days has it been since the last election? "))
            Cvalue = input("Chooce C value? a)custom, b) random, c) default (1.0014), d) back in time ")
            if Cvalue == "a":
                c = float(input("Type c value, recomended value 0.99999 to 1.0001: "))
            elif Cvalue == "random" or Cvalue =="r" or Cvalue =="b":
                c = random.uniform(0.99985,1.0002)
            if Cvalue == "d":
                c = 0.9986
            else:
                c = 1.0014
        elif DoItAll=="b":
            c = random.uniform(0.99985,1.0002)
        population = round(population*c**(DaysSince),0)
        print("The new population is", population)
        total = int(round(population*participationVariableFurther,0))
        participation = round((total/population)*100,2)
        NewCountryPop=NewCountryPop+population
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
                        if SetLikeliness[randomiser] > 0.25:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/5,(SetLikeliness[randomiser])/5),7)
                        elif SetLikeliness[randomiser] <0.26 and SetLikeliness[randomiser] > 0.10:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/3.5,(SetLikeliness[randomiser])/3.5),7)
                        elif SetLikeliness[randomiser] <0.10:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/2.5,(SetLikeliness[randomiser])/2.5),7)
                        elif SetLikeliness[randomiser] <0.01:
                            TheRandom = round(random.uniform(-(SetLikeliness[randomiser])/2,(SetLikeliness[randomiser])/2),7)
                        elif SetLikeliness[randomiser] ==0:
                            TheRandom = 0
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
                            LikelinessRation = Likeliness[0]+Likeliness[1]
                            LikelinessZeroRatio = round(Likeliness[0]/LikelinessRation,2)
                            LikelinessOneRatio = round(Likeliness[1]/LikelinessRation,2)
                            Likeliness[0] = Likeliness[0]-(Diff*LikelinessZeroRatio)
                            Likeliness[1] = Likeliness[1]-(Diff*LikelinessOneRatio)
                            if Likeliness[1] < 0:
                                Likeliness[0] = Likeliness[0] + Likeliness[1] -0.01
                                Likeliness[1] = 0.01
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
            if DoItAll == "a":
                Cheats =input(":) ")
            if Cheats == "random" or Cheats == "r":
                RandomCheat = random.randint(1,20)
            else:
                RandomCheat=0
            if Cheats == "minor" or RandomCheat == 1:
                print("I hope you are over 18! You know... so you can vote!")
                NewAddition = int(round(((HowManyParties/4)*2), 0))
                for New in range(NewAddition):
                    if len(listofparty) > 6:
                        candidature.append(0)
                        candidature[-1]=random.choice([listofparty[-1],listofparty[-2],listofparty[-3],listofparty[-4]])
                    else:
                        fekoff =0
            elif Cheats == "juanma" or RandomCheat == 2:
                print("Female Juanma looks like Olona")
                NewAddition = int(round((HowManyParties/2*1), 0))
                Decider = random.randint(1,2)
                if Decider == 1:
                    CheatPartyOption = random.choice([listofparty[0],listofparty[0],listofparty[1]])
                elif not(Decider == 1):
                    CheatPartyOption = random.choice(listofparty)
                for New in range(NewAddition):
                    candidature.append(CheatPartyOption)
            elif Cheats == "bi" or RandomCheat == 3:
                print("El Bipartidito")
                NewAddition = int(round(((HowManyParties/4)), 0))
                for New in range(NewAddition):
                    candidature.append(0)
                    candidature[-1] = listofparty[0]
                    candidature.append(0)
                    candidature[-1] = listofparty[1]
            elif Cheats == "enforced" or RandomCheat == 4:
                print("You have to vote, NOW")
                total = population
                participation = round((total/population)*100,2)
            elif Cheats == "extreme" or RandomCheat == 5:
                print("This is getting extreme...")
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
                print("Swinging is fun.")
                CheatPartyOption = random.choice(listofparty)
                Swing = numpy.random.choice([2,5,10,15],p=[0.3,0.35,0.25,0.1])
                TimesToAdd = int(round((len(candidature)*Swing)/100,0))
                AddingParties=0
                for AddingParties in range(TimesToAdd):
                    candidature.append(CheatPartyOption)
            elif Cheats == "biased":
                print("Getting a little bit cheaty are we now...")
                CheatPartyOption = int(input("ID of the party to get more votes: "))
                Swing = float(input("Roughly in terms of percentage, how much sould the party increase? "))
                TimesToAdd = int(round((len(candidature)*Swing)/100,0))
                AddingParties=0
                for AddingParties in range(TimesToAdd):
                    candidature.append(CheatPartyOption)
            elif Cheats == "regional":
                print("Regional parties!")
                NumberRegional = int(input("How many regional parties are there here? "))
                RegionalAdd= 0
                for RegionalAdd in range(NumberRegional):
                    CheatPartyOption = int(input("Candidate number of the party to get more votes: "))
                    CheatPartyOption = CheatPartyOption-1
                    OriginalLength = len(candidature)
                    WantedPercentage = float(input("What is the desired percentage for this party? "))
                    NewValue = OriginalLength/(1-(WantedPercentage/100))
                    Amount = int(round(NewValue-OriginalLength,0))
                    AddingParties=0
                    for AddingParties in range(Amount):
                        candidature.append(CheatPartyOption)
            else:
                fekoff = 0
                print("Kri kri kri kri.")
            #print("Candidature", candidature)
        else:
            fekoff = 0
        #print(candidature,candiNum)
    #Allows next part to be done
        check = 0
    #Here is where it runs the elections
        while check != regionSeatsNumber:
    #Part where the elections are done if there are 2 or more seats
            if MethodOfVoting == "a":
                votingnumbersomething = 0
                for votingnumbersomething in range(int(total)):
                    choice = random.choice(candidature)
                    isthisit = 0
                    for isthisit in range(PartyNumber):
                        if choice == listofparty[isthisit]:
                            RegionalVotes[isthisit] = RegionalVotes[isthisit] +1
            elif MethodOfVoting == "b":
                votingnumbersomething = 0
                for votingnumbersomething in range(int(total)):
                    RankedVoting = 0
                    for RankedVoting in range(int(round(PartyNumber/2,0))):
                        PointsToGive = PartyNumber-RankedVoting*2
                        if PointsToGive <=0:
                            PointsToGive = 1
                        choice = random.choice(candidature)
                        isthisit = 0
                        for isthisit in range(PartyNumber):
                            if choice == listofparty[isthisit]:
                                RegionalVotes[isthisit] = RegionalVotes[isthisit] + PointsToGive
            elif MethodOfVoting == "c":
                votingnumbersomething = 0
                for votingnumbersomething in range(int(total)):
                    MultipleVoting =0
                    for MultipleVoting in range (random.randint(1,PartyNumber-1)):
                        choice = random.choice(candidature)
                        isthisit = 0
                        for isthisit in range(PartyNumber):
                            if choice == listofparty[isthisit]:
                                RegionalVotes[isthisit] = RegionalVotes[isthisit] +1
            countingvotes = 0
            for countingvotes in range(PartyNumber):
                TotalVotes[countingvotes] = TotalVotes[countingvotes] + RegionalVotes[countingvotes]
            ValidCounting = 0
            ValidVotes=0
            for ValidCounting in range(PartyNumber-1):
                ValidVotes = ValidVotes+RegionalVotes[ValidCounting]
            if regionSeatsNumber >=2:
    #Runs election
    #Calculates seats for each party
                isthisitseats = 0
                if SeatAlocationMethod == "a": #division proportional
                    for isthisitseats in range(PartyNumber-1):
                        RegionalSeats[isthisitseats] = round((RegionalVotes[isthisitseats]/ValidVotes)*regionSeatsNumber,0)
                        #print(RegionalSeats)
                elif SeatAlocationMethod == "c": #winner takes all
                    CopyingTableT = []
                    CopyingTableTID = 0
                    for CopyingTableTID in range(PartyNumber-1):
                        CopyingTableT.append(RegionalVotes[CopyingTableTID])
                    MaxCand = CopyingTableT.index(max(CopyingTableT))
                    RegionalSeats[MaxCand] = regionSeatsNumber
                elif SeatAlocationMethod == "b": #d'hont
                    Dhont = 0
                    for Dhont in range(int(regionSeatsNumber)):
                        quotientTable  = []
                        for DhontParty in range(PartyNumber-1):
                            quotient = (RegionalVotes[DhontParty])/(RegionalSeats[DhontParty]+1)
                            quotientTable.append(quotient)
                        MaxQuotent = quotientTable.index(max(quotientTable))
                        RegionalSeats[MaxQuotent] = RegionalSeats[MaxQuotent]+1
                elif SeatAlocationMethod == "d": #Sainte-Laguë
                    StL = 0
                    for StL in range(int(regionSeatsNumber)):
                        quotientTable  = []
                        for StLParty in range(PartyNumber-1):
                            quotient = (RegionalVotes[StLParty])/(RegionalSeats[StLParty]*2+1)
                            quotientTable.append(quotient)
                        MaxQuotent = quotientTable.index(max(quotientTable))
                        RegionalSeats[MaxQuotent] = RegionalSeats[MaxQuotent]+1
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
                countingvotesone = 0
                for countingvotesone in range(PartyNumber):
                    TotalVotes[countingvotesone] = TotalVotes[countingvotesone] + RegionalVotes[countingvotesone]
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
        CopyingTableO = []
        CopyingTableOID = 0
        for CopyingTableOID in range(PartyNumber-1):
            CopyingTableO.append(RegionalVotes[CopyingTableOID])
        WinnerRegional = CopyingTableO.index(max(CopyingTableO))
        if ExtraSeatsPercentage !=  0:
            RegionalSeats[WinnerRegional]=RegionalSeats[WinnerRegional]+float(round(regionSeatsNumber*ExtraSeatsPercentage,0))
        print("For region", regionName," the results were:")
        print("Seats to asign:",regionSeatsNumber)
        print("Number of entries", total)
        pringtingregional = 0
        for pringtingregional in range(PartyNumber):
            print(CandidatureName[pringtingregional]," got ", RegionalVotes[pringtingregional], " and ", RegionalSeats[pringtingregional]," seats.")
        print("Participation was", participation, "%.")
        
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
        if AskRegional == 0:
            lines[IdoNotRemember+4] = f'\n"{regionName}",{population},{regionSeatsNumber},{AskRegional}'
        elif AskRegional != 0:
            lines[IdoNotRemember+4] = f'\n"{regionName}",{population},{regionSeatsNumber},{AskRegional},{",".join(str(x) for x in PartiesIDRegionalAmount)},{",".join(str(x) for x in PartyVoteRegionalAmount)}'
#Prints the results for the whole place
lines[0] = f'"{CountryName}",{NewCountryPop},{TotalSeatsCountry}'
lines[1] = f'\n{PartyNumberOriginal}'
lines[2] = f'\n{CompleteNameList}'
lines[3] = f'{CompleteProbabilityList}'
with open('CountryData.txt', 'w') as CountryData:
    CountryData.writelines(lines)
for finalprint in range(PartyNumber):
    print("Total seats for ",CandidatureName[finalprint], " are ",TotalPartySeatNumber[finalprint],". Total votes are",TotalVotes[finalprint],". Number of victories are", Victories[finalprint],".")
print("The new total population is",NewCountryPop)
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