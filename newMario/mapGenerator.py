from os import path
import random
import mapRandom
def load_data(var):
    mapData = []
    gameFolder = path.dirname(__file__)
    if(var%2 == 0):
        mapData = mapRandom.load_data()
    elif var ==1:
        tmp = 'Maps/seg' + str(var) + '.txt'
        with open(path.join(gameFolder,tmp),'rt') as f:
            for line in f:
                mapData.append(line)
    else:
        value = random.randint(1,8)
        tmp = 'Maps/seg' + str(value) + '.txt'
        with open(path.join(gameFolder,tmp),'rt') as f:
            for line in f:
                mapData.append(line)
    return mapData
