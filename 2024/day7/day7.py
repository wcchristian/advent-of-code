import os

def main():
    filename = "day7_input.txt"
    example_filename = "day7_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    lines = read_input(filename)

    sum = 0
    for line in lines:
        if is_equation_valid(line[0], line[1]):
            sum += line[0]

    return sum


def part2(filename):
    lines = read_input(filename)

    sum = 0
    for line in lines:
        if is_equation_valid(line[0], line[1], enable_concat=True):
            sum += line[0]
    
    return sum


def is_equation_valid(value, numbers, enable_concat = False):
    result_set = {0: [numbers[0]]}

    for i in range(1, len(numbers)):
        possible_numbers = []
        for num in result_set[i-1]:
            possible_numbers.append(num + numbers[i])
            possible_numbers.append(num * numbers[i])
            if enable_concat: possible_numbers.append(int(str(num) + str(numbers[i])))
        result_set[i] = possible_numbers


    if value in list(result_set.values())[-1]:
        return True

    return False


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    sanitized_lines = []
    for line in file_lines:
        split = line.split(":")
        value = int(split[0])
        numbers = [int(num) for num in split[1].strip().split(" ")]
        sanitized_lines.append((value, numbers))

    return sanitized_lines


if __name__ == "__main__":
    main()