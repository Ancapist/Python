import random


def load_data():

    def can_jump(x, y):
        print(x - 5," ",y)
        xmin = (x - 4) * (x - 5 > 0)
        xmax = (x + 4) * (x + 5 < 39)
        ymin = y + 1
        ymax = (y + 4)
        if y + 4 > 19: ymax = 19

        if mapArray[y-1][x] != 0:
            return False

        for i in range(xmin, xmax+1):
            for j in range(ymin, ymax+1):
                if mapArray[j][i] == 'B':
                    print("xxx")
                    return True

        return False

    mapArray = [[0] * 49 for i in range(20)]

    for i in range(16,20):
        mapArray[i][0] = 'X'
        mapArray[i][1] = 'X'
        mapArray[i][2] = 'X'

    platform = 3
    height = 0


    while platform < 44:

        height += random.randrange(-3, 4)


        if 16 + height >= 20:
            height -= 3
        elif 16 + height < 0:
            height += 3

        gap = random.randrange(1, 5)

        for j in range(platform, platform + gap):
            mapArray[16 + height][j] = 'B'

        for i in range(platform+1, platform + gap-1):
            if random.randrange(0, 3) == 0:
                mapArray[16 + height - 1][i] = 'S'


        platform += gap

        gap = random.randrange(0,5)

        platform += gap

    for j in range (0,3):
        for i in range(16+j,20):
            mapArray[i][49 - j - 1] = 'X'

    for i in range(15):
        x = random.randrange(0,39)
        y = random.randrange(12,19)
        if mapArray[y][x] == 0 and can_jump(x, y):
            mapArray[y][x] = 'C'

    for i in range(0,49):
        if mapArray[19][i] == 0:
            mapArray[19][i] = 'S'
        for j in range(0,20):
            if mapArray[j][i] == 0:
                mapArray[j][i] = ''

    return mapArray