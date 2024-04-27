import random
import numpy

TotalFor = 0
TotalAga = 0
TotalAbs = 0
PartyFor = 0
PartyAga = 0 
PartyAbs = 0

NumExR = int(input("How many extreme right parties are there? "))
NumRi = int(input("How many rightists parties are there? "))
NumRiC = int(input("How many center right parties are there? "))
NumCen = int(input("How many center parties are there? "))
NumLeC = int(input("How many center left parties are there? "))
NumLe = int(input("How many leftists parties are there? "))
NumExL = int(input("How many extreme left parties are there? "))

PartyIdeology = input("What ideology is the party proposing? ")
Name = input("Name of law? ")
################################################################################################
print("Extreme Right Parties: ")
for ExR in range(int(NumExR)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    RandVal=round(random.uniform(0,0.02),3)
    if PartyIdeology == "extreme left":
        CVf = 0.0+RandVal
        CVa = 1-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(Vote)
    elif PartyIdeology == "left":
        CVf = 0.01+RandVal
        CVa = 0.99-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(Vote)
    elif PartyIdeology == "center-left":
        CVf = 0.01+RandVal
        CVa = 0.97-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.02])
            OptionVote.append(Vote)
    elif PartyIdeology == "center":
        CVf = 0.05+RandVal
        CVa = 0.80-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(Vote)
    elif PartyIdeology == "center-right":
        CVf = 0.35+RandVal
        CVa = 0.45-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(Vote)
    elif PartyIdeology == "right":
        CVf = 0.6+RandVal
        CVa = 0.1-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.3])
            OptionVote.append(Vote)
    elif PartyIdeology == "extreme right":
        CVf = 0.95+RandVal
        CVa = 0.02-RandVal
        for i in range(int(25)):
            Vote = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.03])
            OptionVote.append(Vote)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
###########################################################################################################
print("Right Parties: ")
for Rig in range(int(NumRi)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CtiB=round(random.uniform(-0.1,0.1),3)
    if PartyIdeology == "extreme left":
        CVf = 0.1+CtiB
        CVa = 0.9-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "left":
        CVf = 0.15+CtiB
        CVa = 0.75-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-left":
        CVf = 0.2+CtiB
        CVa = 0.65-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center":
        CVf = 0.4+CtiB
        CVa = 0.4-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-right":
        CVf = 0.7+CtiB
        CVa = 0.1-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "right":
        CVf = 0.75+CtiB
        CVa = 0.1-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "extreme right":
        CVf = 0.1+CtiB
        CVa = 0.8-CtiB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
##############################################################################################################
print("Center Right Parties: ")
for CenR in range(int(NumRiC)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CtrB=round(random.uniform(-0.1,0.1),3)
    if PartyIdeology == "extreme left":
        CVf = 0.1+CtrB
        CVa = 0.9-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "left":
        CVf = 0.15+CtrB
        CVa = 0.75-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-left":
        CVf = 0.2+CtrB
        CVa = 0.65-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center":
        CVf = 0.4+CtrB
        CVa = 0.4-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-right":
        CVf = 0.75+CtrB
        CVa = 0.1-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "right":
        CVf = 0.6+CtrB
        CVa = 0.1-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.3])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "extreme right":
        CVf = 0.1+CtrB
        CVa = 0.8-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
###################################################################################################################
print("Center Parties: ")
for Cen in range(int(NumCen)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CtrB=round(random.uniform(-0.1,0.1),3)
    if PartyIdeology == "extreme left":
        CVf = 0.1+CtrB
        CVa = 0.9-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "left":
        CVf = 0.3+CtrB
        CVa = 0.4-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.4])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-left":
        CVf = 0.5+CtrB
        CVa = 0.1-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.4])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center":
        CVf = 0.4+CtrB
        CVa = 0.4-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-right":
        CVf = 0.5+CtrB
        CVa = 0.1-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.4])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "right":
        CVf = 0.3+CtrB
        CVa = 0.4-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.3])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "extreme right":
        CVf = 0.1+CtrB
        CVa = 0.9-CtrB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCt)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
############################################################################################################
print("Center Left Parties: ")
for LeC in range(int(NumLeC)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CoiB=round(random.uniform(-0.1,0.1),3)
    if PartyIdeology == "extreme left":
        CVf = 0.1+CoiB
        CVa = 0.9-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "left":
        CVf = 0.6+CoiB
        CVa = 0.2-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center-left":
        CVf = 0.8+CoiB
        CVa = 0.1-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center":
        CVf = 0.4+CoiB
        CVa = 0.4-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center-right":
        CVf = 0.25+CoiB
        CVa = 0.5-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.25])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "right":
        CVf = 0.2+CoiB
        CVa = 0.6-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "extreme right":
        CVf = 0.1+CoiB
        CVa = 0.8-CoiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCo)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
#########################################################################################################
print("Left Parties: ")
for Lef in range(int(NumLe)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CfiB=round(random.uniform(-0.1,0.1),3)
    if PartyIdeology == "extreme left":
        CVf = 0.2+CfiB
        CVa = 0.8-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "left":
        CVf = 0.8+CfiB
        CVa = 0.1-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center-left":
        CVf = 0.7+CfiB
        CVa = 0.15-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center":
        CVf = 0.4+CfiB
        CVa = 0.4-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "center-right":
        CVf = 0.15+CfiB
        CVa = 0.6-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.25])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "right":
        CVf = 0.1+CfiB
        CVa = 0.7-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCo)
    elif PartyIdeology == "extreme right":
        CVf = 0.1+CfiB
        CVa = 0.8-CfiB
        for i in range(int(25)):
            VoteRCo = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCo)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs
##########################################################################################################
print("Extreme Left Parties: ")
for LeX in range(int(NumExL)):
    Rv = 0
    PartyFor = 0
    PartyAga = 0 
    PartyAbs = 0
    OptionVote = []
    i = 0
    PartyName = input("Name of the party? ")
    Seats = int(input("How many seats does the party have? "))
    CeB=round(random.uniform(-0.1,0.15),3)
    if PartyIdeology == "extreme left":
        CVf = 0.9+CeB
        CVa = 0.1-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "left":
        CVf = 0.75+CeB
        CVa = 0.15-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-left":
        CVf = 0.65+CeB
        CVa = 0.2-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.15])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center":
        CVf = 0.2+CeB
        CVa = 0.6-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "center-right":
        CVf = 0.1+CeB
        CVa = 0.7-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.2])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "right":
        CVf = 0.1+CeB
        CVa = 0.8-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    elif PartyIdeology == "extreme right":
        CVf = 0+CeB
        CVa = 0.9-CeB
        for i in range(int(25)):
            VoteRCt = numpy.random.choice(["for","against","abstain"], p = [CVf,CVa,0.1])
            OptionVote.append(VoteRCt)
    for Rv in range(int(Seats)):
        Ptvote = random.choice(OptionVote)
        if Ptvote == "for":
            PartyFor=PartyFor+1
        elif Ptvote == "against":
            PartyAga=PartyAga+1
        elif Ptvote == "abstain":
            PartyAbs=PartyAbs+1
        
    print(PartyName,"voted:",PartyFor,"votes for.",PartyAga,"votes against and",PartyAbs," abstains.")
    TotalFor = TotalFor + PartyFor
    TotalAga = TotalAga + PartyAga
    TotalAbs = TotalAbs + PartyAbs

NeedPass=(TotalFor+TotalAga+TotalAbs)/2
print("Number of votes for needed to pass the law are",NeedPass,"votes.")
print("The result of the voting for the law",Name,"are:")
print("Total for:",TotalFor)
print("Total against:",TotalAga)
print("Total absentions:",TotalAbs)
if TotalFor>= int(NeedPass):
    print("Passed succesfully with Mayority.")
elif TotalFor < int(NeedPass):
    if TotalFor > TotalAga:
        print("Passed succesfully with simple mayority")
    elif TotalFor<TotalAga:
        print("Passed unsuccesfully.")
    if TotalAbs+TotalFor == TotalAga:
        print("Law has to be re-ran.")