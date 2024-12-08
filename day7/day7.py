inputFile = "input.txt"
equations = []
with open(inputFile, 'r') as f:
    for line in f:
        split1 = line.strip('\n').split(':')
        testValue = int(split1[0])
        parts = list(map(int, split1[1].strip(' ').split(' ')))
        equations.append((testValue, parts))

result = 0
wrongEquations = []
for equation in equations:
    testValue = equation[0]
    parts = equation[1]

    isCorrect = True
    potentialValues = {parts[0]}
    for i in range(1, len(parts), 1):
        newPotentialValues = set()
        for potentialValue in potentialValues:
            sum = potentialValue + parts[i]
            mul = potentialValue * parts[i]

            if sum > testValue and mul > testValue:
                continue
            if sum <= testValue:
                newPotentialValues.add(sum)
            if mul <= testValue:
                newPotentialValues.add(mul)
        if len(newPotentialValues) == 0:
            isCorrect = False
            break

        potentialValues = newPotentialValues
        
    if isCorrect and testValue in potentialValues:
        result += testValue
    else:
        wrongEquations.append(equation)
       
print(result)

# part 2

for equation in wrongEquations:
    testValue = equation[0]
    parts = equation[1]

    isCorrect = True
    potentialValues = {parts[0]}
    for i in range(1, len(parts), 1):
        newPotentialValues = set()
        for potentialValue in potentialValues:
            sum = potentialValue + parts[i]
            mul = potentialValue * parts[i]
            dig = int(str(potentialValue) + str(parts[i]))

            if sum > testValue and mul > testValue and dig > testValue:
                continue
            if sum <= testValue:
                newPotentialValues.add(sum)
            if mul <= testValue:
                newPotentialValues.add(mul)
            if dig <= testValue:
                newPotentialValues.add(dig)

        if len(newPotentialValues) == 0:
            isCorrect = False
            break

        potentialValues = newPotentialValues
        
    if isCorrect and testValue in potentialValues:
        result += testValue

print(result)