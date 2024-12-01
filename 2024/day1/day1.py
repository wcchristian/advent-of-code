import os
import re

def main():
    filename = "day1_input.txt"
    example_filename = "day1_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    list_one, list_two = read_input(filename)
    return sum([abs(list_one[i] - list_two[i]) for i in range(0, len(list_one))])


def part2(filename):
    list_one, list_two = read_input(filename)
    return sum([list_one[idx] * len([x for x in list_two if x == list_one[idx]]) for idx in range(0, len(list_one))])


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    list_one = [int(re.split(r"\s+", line)[0]) for line in file_lines]
    list_two = [int(re.split(r"\s+", line)[1]) for line in file_lines]
    list_one.sort()
    list_two.sort()

    return list_one, list_two


if __name__ == "__main__":
    main()