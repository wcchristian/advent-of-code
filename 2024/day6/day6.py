import os


direction_map = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0)
}

next_direction = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

def main():
    filename = "day6_input.txt"
    example_filename = "day6_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)
    guard_start_loc = find_guard(grid)
    visited_list = set()
    current_position = guard_start_loc
    visited_list.add(current_position)
    current_direction = grid[guard_start_loc[0]][guard_start_loc[1]]

    for i in range(10_000):
        next_y = current_position[0] + direction_map[current_direction][0]
        next_x = current_position[1] + direction_map[current_direction][1]

        try:
            if grid[next_y][next_x] == "#":
                current_direction = next_direction[current_direction]
            else:
                current_position = (next_y, next_x)
                visited_list.add((next_y, next_x))

        except IndexError as e:
            break

    return len(visited_list)


def part2(filename):
    lines = read_input(filename)

    # For each open space on the grid.
        # place an obstruction
        # Run the "Simulation"
            # IF we step on the same path multiple times? OR something
            # Then we know that it's a loop
            # Add the point to the "Confirmed points" list

    return 0

def find_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in "^<>vV":
                return y, x
    return -1, -1


def print_grid(grid, visited_locations):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) in visited_locations:
                print("X", end="")
            else:
                print(grid[y][x], end="")

            if x == len(grid[y]) - 1:
                print()
    print("\n")


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    grid = file.readlines()

    return [line.strip() for line in grid]


if __name__ == "__main__":
    main()
