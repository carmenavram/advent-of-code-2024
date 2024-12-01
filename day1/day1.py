leftList = []
rightList = []

with open('input.txt', 'r') as f:
    for line in f:
        fields = line.strip().split('   ')
        num1 = int(fields[0])
        num2 = int(fields[1])  
        leftList.append(num1)
        rightList.append(num2)

# part 1
leftList.sort()
rightList.sort()
sum = 0
for i in range(len(leftList)):
    sum += abs(leftList[i] - rightList[i])
    
print(sum)

# part 2
similarityScore = 0
numberOcurrence = dict()
for rightItem in rightList:
    if rightItem in numberOcurrence:
        numberOcurrence[rightItem] = numberOcurrence[rightItem] + 1
    else:
        numberOcurrence[rightItem] = 1

for leftItem in leftList:
    if leftItem in numberOcurrence:
        similarityScore += leftItem * numberOcurrence[leftItem]

print(similarityScore)