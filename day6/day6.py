import numpy as np

def getNextPoint(currentPoint, direction):
    return (currentPoint[0] + direction[0], currentPoint[1] + direction[1])

def getPrevPoint(currentPoint, direction):
    return (currentPoint[0] - direction[0], currentPoint[1] - direction[1])

def changeDirection(direction):
     newDirection = (0,0)
     match direction:
            case (-1,0): newDirection = (0,1)
            case (1,0): newDirection = (0,-1)
            case (0, -1): newDirection = (-1,0)
            case (0, 1): newDirection = (1,0)
            case _: print("error")
     return newDirection

map = []
mapSize = 0
startPoint = (0,0)
with open('inputExample.txt', 'r') as f:
    mapSize = sum(1 for _ in f)
    map = np.empty(shape=(mapSize,mapSize),dtype=str)

with open('inputExample.txt', 'r') as f:
    i = 0
    for line in f:
        j = 0
        map[i] = line.strip('\n')
        for ch in line.strip('\n'):
            map[i][j] = ch
            if ch == '^': 
                startPoint = (i,j)
                map[i][j] = '.'
            j += 1
        i += 1

result = 0
markedPoints = {startPoint}
obstacles = set()
currentPoint = (startPoint[0] - 1, startPoint[1])
direction = (-1,0)
while currentPoint[0] < mapSize and currentPoint[1] < mapSize and currentPoint[0] > -1 and currentPoint[1] > -1:
    if (map[currentPoint[0]][currentPoint[1]]) == '.':
        # check if could be obstacte
        prevPoint = getPrevPoint(currentPoint, direction)
        newDirection = changeDirection(direction)
        nextPoint = getNextPoint(prevPoint, newDirection)
        if nextPoint in markedPoints:
            obstacles.add(currentPoint)

        markedPoints.add(currentPoint)
        currentPoint = getNextPoint(currentPoint, direction)
    else:
        prevPoint = getPrevPoint(currentPoint, direction)
        direction = changeDirection(direction)
        currentPoint = getNextPoint(prevPoint, direction)

result = len(markedPoints)
print(result)

# part 2

result = len(obstacles)

print(result)
