import os
import re
import math

def main():
    filename = "day3_input.txt"
    example_filename = "day3_example.txt"
    example_2_filename = "day3_2_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 2: {part1(filename)}')
    print(f'Part 1 Example: {part2(example_2_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    line = read_input(filename)
    return find_sum_of_multiples(line)


def part2(filename):
    line = read_input(filename)
    valid_line = ""
    dont_split = line.split('don\'t()')
    valid_line += dont_split[0]

    for line in dont_split[1:]:
        do_split = line.split("do()")
        valid_line += "".join(do_split[1:])

    return find_sum_of_multiples(valid_line)


def find_sum_of_multiples(line):
    pattern = re.compile(r'mul\(\d+,\d+\)')
    multiples = pattern.findall(line)

    num_pattern = re.compile("\d+")
    sum = 0
    for multiple in multiples:
        nums = num_pattern.findall(multiple)
        sum += math.prod([int(x) for x in nums])

    return sum


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_text = file.read()

    return file_text


if __name__ == "__main__":
    main()