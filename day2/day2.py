
def isSafeReport(levels):
    levelsCopy = levels.copy()
    levelsCopy.sort()
    isAscending = levelsCopy == levels
    isDescending = False
    if isAscending == False:
        levelsCopy.sort(reverse=True)
        isDescending = levelsCopy == levels
    isSafeReport = isAscending or isDescending
    if isAscending or isDescending:
        for i in range(1, len(levels), 1):
            diff = abs(levels[i] - levels[i-1])
            if diff < 1 or diff > 3:
                return False
            else:
                isSafeReport = isSafeReport and True
    return isSafeReport

reports = []

with open('input.txt', 'r') as f:
    for line in f:
        levels = []
        levelsString = line.strip().split(' ')
        for l in levelsString:
            levels.append(int(l))
        reports.append(levels)

safeReportsCount = 0
notSafeReports1 = []
for levels in reports:
    if isSafeReport(levels):
        safeReportsCount += 1
    else:
        notSafeReports1.append(levels)

print(safeReportsCount)

# part 2

for levels in notSafeReports1:
    isSafe = False
    for el in range(len(levels)):
        newLevels = levels[:el] + levels[el+1:]
        if isSafeReport(newLevels):
            isSafe = True
            break  
    if isSafe:
        safeReportsCount += 1

print(safeReportsCount)
