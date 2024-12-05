import os

neighbor_direction_tuple_map = {
    "N": (-1, 0),
    "NE": (-1, 1),
    "E": (0, 1),
    "SE": (1, 1),
    "S": (1, 0),
    "SW": (1, -1),
    "W": (0, -1),
    "NW": (-1, -1)
}

diag_neighbor_direction_tuple_map = {
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "NW": (-1, -1)
}

neighbor_compliment = {
    "NE": "SW",
    "SE": "NW",
    "SW": "NE",
    "NW": "SE"
}

next_letter_map = {
    "X": "M",
    "M": "A",
    "A": "S",
    "S": None
}

def main():
    filename = "day4_input.txt"
    example_filename = "day4_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    grid = read_input(filename)

    # Find X
    counter = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                counter += depth_first_search_for_christmas((y, x), grid)

    return counter


def part2(filename):
    grid = read_input(filename)

    # Find A
    counter = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'A':
                mas_counter = 0
                for direction in diag_neighbor_direction_tuple_map:
                    new_coord = add_direction_to_coord((y, x), direction)
                    opposite_coord = add_direction_to_coord((y, x), neighbor_compliment[direction])

                    if new_coord[0] < 0 or new_coord[0] >= len(grid) or new_coord[1] < 0 or new_coord[1] >= len(grid[0]):  ## If Out of Range
                        continue

                    if opposite_coord[0] < 0 or opposite_coord[0] >= len(grid) or opposite_coord[1] < 0 or opposite_coord[1] >= len(grid[0]):  ## If Out of Range
                        continue

                    if grid[new_coord[0]][new_coord[1]] == "M" and grid[opposite_coord[0]][opposite_coord[1]] == "S":
                        mas_counter += 1

                if mas_counter >= 2:
                    counter += 1

    return counter

def depth_first_search_for_christmas(coord, grid):
    counter = 0
    for direction in neighbor_direction_tuple_map:
        if does_direction_contain_full_string(coord, grid, direction, 'M'):
            counter += 1

    return counter

def add_direction_to_coord(coord, direction):
    return coord[0] + neighbor_direction_tuple_map[direction][0], coord[1] + neighbor_direction_tuple_map[direction][1]

def does_direction_contain_full_string(coord, grid, direction, goal_letter):
    next_goal_letter = next_letter_map[goal_letter]
    new_coord = add_direction_to_coord(coord, direction)

    if new_coord[0] < 0 or new_coord[0] >= len(grid) or new_coord[1] < 0 or new_coord[1] >= len(grid[0]): ## If Out of Range
        return False

    if grid[new_coord[0]][new_coord[1]] == "S" and goal_letter == "S": # If Found final letter
        return True

    if grid[new_coord[0]][new_coord[1]] == goal_letter: # If found next letter but not final Letter
        return does_direction_contain_full_string(new_coord, grid, direction, next_goal_letter)
    else: # Did not find next letter
        return False


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    raw_grid = file.readlines()
    sanitized_grid = [line.strip() for line in raw_grid]

    return sanitized_grid


if __name__ == "__main__":
    main()