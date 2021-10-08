import random

def shufflenames(names):
    numplayers = len(names)
    randnames = []
    for name in names:
        randname = names[(random.randint(0, numplayers-1))]
        if randname not in randnames:
            randnames.append(randname)
        else:
            while(randname in randnames):
                randname = names[(random.randint(0, numplayers-1))]
            randnames.append(randname)

    print(F"PLAYER LIST: {randnames}\n")
    return randnames

def splitnames(roster):
    team1 = []
    team2 = []
    numplayers = len(roster)
    if numplayers % 2 == 1:
        print("WARNING: Odd number of players so teams will be uneven")
    for i in range(numplayers):
        if i % 2 == 0:
            team1.append(roster[i])
        else:
            team2.append(roster[i])

    print(f"TEAM 1: {team1}\n\nTEAM 2: {team2}")

if __name__ == "__main__":
    
    names = []
    numplayers = 0
    with open("teamgen_input.txt", 'r') as namesfile:
        for line in namesfile:
            names.append(line.strip())

    #numteams = int(input("How many teams are being divided? "))
    splitnames(shufflenames(names))