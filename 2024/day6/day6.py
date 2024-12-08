import os
from collections import Counter

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
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)
    visited_counter = find_unique_places_in_grid(grid)
    return len(visited_counter)


def part2(filename):
    grid = read_input(filename)
    obstacle_grids = make_obstacle_grids(grid)

    counter = 0
    for z in range(len(obstacle_grids)):
        visited_counter, is_loop = find_unique_places_in_grid_p2(obstacle_grids[z])

        if is_loop:
            counter += 1

    return counter


def find_unique_places_in_grid(grid):
    guard_start_loc = find_guard(grid)
    current_position = guard_start_loc
    current_direction = grid[guard_start_loc[0]][guard_start_loc[1]]

    visited_counter = Counter()
    visited_counter[current_position] += 1

    while True:
        next_y = current_position[0] + direction_map[current_direction][0]
        next_x = current_position[1] + direction_map[current_direction][1]

        if next_x < 0 or next_x > len(grid[0]) - 1 or next_y < 0 or next_y > len(grid) - 1: # If outside of the grid limits, break
            break

        if grid[next_y][next_x] == "#": # If we encounter an obstacle, change direction
            current_direction = next_direction[current_direction]

        else: # Else we did NOT encounter an obstacle, move forward and add the position to the counter
            current_position = (next_y, next_x)
            visited_counter[(next_y, next_x)] += 1

    return visited_counter


def find_unique_places_in_grid_p2(grid):
    current_position = find_guard(grid)
    current_direction = grid[current_position[0]][current_position[1]]

    visited_counter = Counter()
    visited_counter[(current_direction, current_position)] += 1

    is_loop = False

    while True:
        next_y = current_position[0] + direction_map[current_direction][0]
        next_x = current_position[1] + direction_map[current_direction][1]

        if next_x < 0 or next_x > len(grid[0]) - 1 or next_y < 0 or next_y > len(grid) - 1:  # If outside of the grid limits, break
            break

        if grid[next_y][next_x] == "#":  # If we encounter an obstacle, change direction
            current_direction = next_direction[current_direction]
            visited_counter[(current_direction, (next_y, next_x))] += 1
            continue

        else: # Else we did NOT encounter an obstacle, move forward and add the position to the counter
            current_position = (next_y, next_x)
            visited_counter[(current_direction, (next_y, next_x))] += 1

        if (current_direction, (next_y, next_x)) in visited_counter.keys() and visited_counter[(current_direction, (next_y, next_x))] > 1: #If we have already visited this spot more than once, it's a loop, break
            is_loop = True
            break

    return visited_counter, is_loop


def find_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in "^<>vV":
                return y, x
    return -1, -1


def make_obstacle_grids(grid):
    visited_counter = find_unique_places_in_grid(grid)
    no_first_step = dict(list(visited_counter.items())[1:])

    grid_list = []
    for step in no_first_step:
        grid_copy = grid.copy()
        string_list = list(grid_copy[step[0]])
        string_list[step[1]] = "#"
        grid_copy[step[0]] = "".join(string_list)
        grid_list.append(grid_copy)

    return grid_list


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    grid = file.readlines()

    return [line.strip() for line in grid]


if __name__ == "__main__":
    main()
