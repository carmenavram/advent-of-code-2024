import numpy as np

def printMap(map, mapSize):
    for i in range(mapSize):
        for j in range(mapSize):
            print(map[i][j], end="")
        print("\n", end="")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

def isPointValid(point, size):
    return point.x < size and point.y < size and point.x > -1 and point.y > -1

map = []
mapSize = 0
inputFile = "input.txt"
with open(inputFile, 'r') as f:
    mapSize = sum(1 for _ in f)
    map = np.empty(shape=(mapSize,mapSize),dtype=str)

antennas = dict()
with open(inputFile, 'r') as f:
    i = 0
    for line in f:
        j = 0
        map[i] = line.strip('\n')
        for ch in line.strip('\n'):
            map[i][j] = ch
            if ch != '.':
                if ch in antennas:
                    antennas[ch].append(Point(i, j))
                else:
                    antennas[ch] = [Point(i, j)]
            j += 1
        i += 1

#printMap(map, mapSize)

antinodes = set()
for i in antennas:
    for j in range(len(antennas[i])):
        for k in range(j + 1, len(antennas[i]), 1):
            antenna1 = antennas[i][j]
            antenna2 = antennas[i][k]
            difX = antenna1.x - antenna2.x
            difY = antenna1.y - antenna2.y
            antinode1 = Point(antenna1.x + difX, antenna1.y + difY)
            antinode2 = Point(antenna2.x - difX, antenna2.y - difY)
            if isPointValid(antinode1, mapSize): antinodes.add(antinode1)
            if isPointValid(antinode2, mapSize): antinodes.add(antinode2)

result = len(antinodes)
       
print(result)

# part 2

antinodes = set()
for i in antennas:
    for j in range(len(antennas[i])):
        for k in range(j + 1, len(antennas[i]), 1):
            antenna1 = antennas[i][j]
            antenna2 = antennas[i][k]
            difX = antenna1.x - antenna2.x
            difY = antenna1.y - antenna2.y
            point = antenna1
            while isPointValid(point, mapSize):
                antinodes.add(point)
                point = Point(point.x + difX, point.y + difY)
            point = antenna2
            while isPointValid(point, mapSize):
                antinodes.add(point)
                point = Point(point.x - difX, point.y - difY)

result = len(antinodes)

print(result)