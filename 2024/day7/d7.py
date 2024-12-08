def possible(subtotal, i): return True if i == len(numbers) and subtotal == value else False if subtotal > value or i == len(numbers) else possible(subtotal * numbers[i], i + 1) or possible(subtotal + numbers[i], i + 1)
total = 0
for line in open(0):
    value, numbers = int(line[:line.find(':')]), [int(n) for n in line[line.find(':') + 2:].split()]
    total += value if possible(numbers[0],1) else 0
print(total)





from collections import defaultdict

input = [l.strip() for l in open('input.txt') if l.strip() != '']


def op1(a, b): return a+b
def op2(a, b): return a*b
def op3(a, b): return int(str(a) + str(b))


def solveEquation(equation, target, operations):
    allResults = defaultdict(set)

    allResults[0] = {equation[0]}

    for i in range(1, len(equation)):
        possibleResults = set()
        for prevResult in allResults[i-1]:
            for op in operations:
                result = op(prevResult, equation[i])

                if result <= target:
                    possibleResults.add(result)

        if len(possibleResults) == 0 or min(possibleResults) > target:
            break
        allResults[i] = possibleResults

    return target in allResults[len(equation) - 1]


operations = [op1, op2, op3]
result = 0
for line in input:
    l = line.split(':')
    target = int(l[0])
    equation = list(map(int, l[1].split()))
    if solveEquation(equation, target, operations):
        result += target

print(result)