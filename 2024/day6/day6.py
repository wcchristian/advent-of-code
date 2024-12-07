import os


direction_map = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

def main():
    filename = "day6_input.txt"
    example_filename = "day6_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)
    print_grid(grid)
    guard_start_loc = find_guard(grid)
    oob = False
    while not oob:
        try:
            # check forward
            # If it's a wall, change direction
            # If it's not a wall, walk there
            # store current location IF not already in visited list

        except:
            oob = False


    print(guard_start_loc)

    # output, just find the len of the list of the visited space array.
    return 0


def part2(filename):
    lines = read_input(filename)

    return 0

def find_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in "^<>vV":
                return y, x
    return -1, -1


def print_grid(grid):
    for line in grid:
        print(line, end='')
    print("\n")

def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    grid = file.readlines()

    return grid


if __name__ == "__main__":
    main()