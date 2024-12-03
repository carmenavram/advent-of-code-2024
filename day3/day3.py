
import re

class Index:
    def __init__(self, startIndex, type):
        self.startIndex = startIndex
        self.type = type

def getMultiplyFromMul(match):
    numbers = str(match)[4:].strip(')').split(',')
    return int(numbers[0]) * int(numbers[1])

result = 0

with open('input.txt', 'r') as f:
    for line in f:
        pattern = r'mul\(\d+\,\d+\)'
        for match in re.findall(pattern, line):
            result += getMultiplyFromMul(match)

print(result)

# part 2

result = 0
with open('input.txt', 'r') as f:
    content = f.read()
    patternMul = r'mul\(\d+\,\d+\)'
    patternDont = r'don\'t\(\)'
    patternDo = r'do\(\)'

    indexes = []
    mulDict = dict()
    mulMatches = re.finditer(patternMul, content)
    for match in mulMatches:
        indexes.append(Index(match.start(), 'mul'))
        mulDict[match.start()] = match.group()

    dontMatches = re.finditer(patternDont, content)
    for match in dontMatches:
        indexes.append(Index(match.start(), 'dont'))

    doMatches = re.finditer(patternDo, content)
    for match in doMatches:
        indexes.append(Index(match.start(), 'do')) 

    indexes.sort(key=lambda x: x.startIndex)
    for i in range(len(indexes)):
        if indexes[i].type == 'mul':
            if i == 0 or indexes[i-1].type == 'do' or indexes[i-1].type == 'mul':
                result += getMultiplyFromMul(mulDict[indexes[i].startIndex])
            else:
                indexes[i].type = 'dont'

print(result)
