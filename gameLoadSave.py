import csv
from Character import *

def loadPlayer(playerName):
    arr = []
    with open(playerName + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for line in reader:
            arr.append(line)

        p = Player()
        p.playerName = arr[0]
        p.playerHealth = int(arr[1])
        p.playerDamage = int(arr[2])
        p.playerWeaponName = arr[3]

def savePlayer(playerData):
    with open(playerData[0] + '.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(playerData[0])
        writer.writerow(str(playerData[1]))
        writer.writerow(str(playerData[2]))
        writer.writerow(playerData[3])


