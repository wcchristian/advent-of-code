import os
import re

def main():
    filename = "day0_input.txt"
    example_filename = "day0_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    list_one, list_two = read_input(filename)
    diff_list = [abs(list_one[i] - list_two[i]) for i in range(0, len(list_one))]
    return sum(diff_list)


def part2(filename):
    list_one, list_two = read_input(filename)
    overall_score = 0

    for idx in range(0, len(list_one)):
        num = list_one[idx]
        times_in_list_two = len([x for x in list_two if x == num])
        overall_score += (num * times_in_list_two)

    return overall_score


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