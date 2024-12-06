def getMiddleElement(update):
    return update[len(update) // 2]

def isCorrect(update):
    isCorrect = True
    for i in range(len(update)):
        beforeSet = set(update[:i])
        afterSet = set(update[i+1:])
        pageNumber = update[i]
        if pageNumber in numbersBefore and beforeSet.issubset(numbersBefore[pageNumber]) == False:
            isCorrect = False
            break
        elif pageNumber in numbersAfter and afterSet.issubset(numbersAfter[pageNumber]) == False:
            isCorrect = False
            break
    return isCorrect

result = 0
incorrectUpdates = []
updates = []
numbersBefore = dict()
numbersAfter = dict()
with open('input.txt', 'r') as f:
    for line in f:
        if '|' in line:
            pageOrders = line.strip('\n').split('|')
            pageNumberLeft = int(pageOrders[0])
            pageNumberRight = int(pageOrders[1])
            if pageNumberRight in numbersBefore:
                numbersBefore[pageNumberRight].add(pageNumberLeft)
            else:
                numbersBefore[pageNumberRight] = {pageNumberLeft}
            if pageNumberLeft in numbersAfter:
                numbersAfter[pageNumberLeft].add(pageNumberRight)
            else:
                numbersAfter[pageNumberLeft] = {pageNumberRight}
        elif ',' in line:
            updates.append(list(map(int, line.strip('\n').split(','))))

for update in updates:
    if isCorrect(update):
        result += getMiddleElement(update)
    else:
        incorrectUpdates.append(update)

print(result)

# part 2

result = 0
for update in incorrectUpdates:
    halfLength = len(update) // 2
    for i in range(len(update)):
        pageNumber = update[i]
        numbersBeforeSeq = []
        numbersAfterSeq = []
        updateSet = set(update)
        if pageNumber in numbersBefore:
            numbersBeforeSeq = numbersBefore[pageNumber].intersection(updateSet)
        if pageNumber in numbersAfter:
            numbersAfterSeq = numbersAfter[pageNumber].intersection(updateSet)
        if len(numbersBeforeSeq) == halfLength and len(numbersAfterSeq) == halfLength:
            result += pageNumber
            break

print(result)
