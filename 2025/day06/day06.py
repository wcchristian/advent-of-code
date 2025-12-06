from pathlib import Path
import re

def main():
    filename = "day06_input.txt"
    example_filename = "day06_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    lines = read_file(filename)
    problems, operators = parse_problems_part_1(lines)
    solved_problems = solve_problems(problems, operators)
    return sum(solved_problems)

def part2(filename):
    lines = read_file(filename)
    problems, operators = parse_problems_part_2(lines)
    solved_problems = solve_problems(problems, operators)
    return sum(solved_problems)


def parse_problems_part_1(lines):
    parsed_problems = []

    for line in lines[:-1]:
        num_problems = [x.strip() for x in re.findall(r'\d* *', line) if x != '']
        sanitized = [x for x in num_problems if x != '']
        parsed_problems.append(sanitized)


    operator_list = [x.strip() for x in re.findall(r'[*+]', lines[-1])]
    sanitized_operator_list = [x for x in operator_list if x != '']
    
    problems = []
    for i in range(len(parsed_problems[0])):
        numbers = []
        for j in range(len(parsed_problems)):
            numbers.append(int(parsed_problems[j][i]))
        problems.append(numbers)

    return problems, sanitized_operator_list


def parse_problems_part_2(lines):
    problem = []
    problems = []
    for col in reversed(range(len(lines[0]))):
        num = ''
        for row in range(len(lines[:-1])):
            num += lines[row][col]
        
        if(num.strip() != ''):
            problem.append(num)
        else:
            problems.append(problem)
            problem = []

    problems.append(problem)

    operator_list = [x.strip() for x in re.findall(r'[*+]', lines[-1])]
    sanitized_operator_list = [x for x in operator_list if x != '']
    
    sanitized_problems = []
    for problem in problems:
        sanitized_problems.append([int(x.strip()) for x in problem if x.strip() != ''])

    return sanitized_problems, list(reversed(sanitized_operator_list))


def solve_problems(problems, operators):
    results = []
    for i in range(len(problems)):
        if operators[i] == '+':
            results.append(sum(problems[i]))
        elif operators[i] == "*":
            product = problems[i][0]
            for number in problems[i][1:]:
                product *= number
            results.append(product)

    return results


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return data


if __name__ == "__main__":
    main()