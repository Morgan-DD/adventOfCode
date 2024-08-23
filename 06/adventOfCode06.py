#
# Advent of code 06
#
time = [63, 78, 94, 68]
distance = [411, 1274, 2047, 1035]

totalPosibilitys = 0

idRace = 0
possibility = 0
for raceTime in time:
    raceDistance = distance[idRace]
    print(str(raceTime) + " | " +  str(raceDistance))
    idRace+=1
    for i in range(raceTime):
        if(i*(raceTime-i) > raceDistance):
            print(str(i) + " * " + str(raceTime-i))
    if(possibility)
    possibility = 0