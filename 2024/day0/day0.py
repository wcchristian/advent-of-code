import os

def main():
    filename = "day0_input.txt"
    example_filename = "day0_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    lines = read_input(filename)

    return 0


def part2(filename):
    lines = read_input(filename)

    return 0


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    return file_lines


if __name__ == "__main__":
    main()