from math import lcm
import os

def main():
    filename = "day8_input.txt"
    example_filename = "day8_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)
    antinodes = set()
    antenna_dict = dict()

    # Find all of the antennas
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].isalnum():
                if not grid[y][x] in antenna_dict:
                    antenna_dict[grid[y][x]] = []
                antenna_dict[grid[y][x]].append((y, x))

    # Find all antinodes
    for item in antenna_dict.items():
        for coord in item[1]:
            for antenna in item[1]:
                y_distance = coord[0] - antenna[0]
                x_distance = coord[1] - antenna[1]
                antenna_distance = (y_distance, x_distance)
                if antenna_distance != (0, 0):
                    antinode_y = coord[0] + y_distance
                    antinode_x = coord[1] + x_distance

                    # if in bounds
                    if antinode_y >= 0 and antinode_y <= len(grid) - 1 and antinode_x >= 0 and antinode_x <= len(grid[0]) - 1:
                        antinodes.add((antinode_y, antinode_x))

    return len(antinodes)


def part2(filename):
    grid = read_input(filename)
    antinodes = set()
    antenna_dict = dict()

    # Find all of the antennas
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].isalnum():
                if not grid[y][x] in antenna_dict:
                    antenna_dict[grid[y][x]] = []
                antenna_dict[grid[y][x]].append((y, x))


    # Find all antinodes
    for item in antenna_dict.items():
        for coord in item[1]:
            for antenna in item[1]:
                y_distance = coord[0] - antenna[0]
                x_distance = coord[1] - antenna[1]
                if not y_distance == 0 and not x_distance == 0: # If this is NOT the same space that we started
                    antinode_y = coord[0]
                    antinode_x = coord[1]

                    # if in bounds
                    while antinode_y >= 0 and antinode_y < len(grid) and antinode_x >= 0 and antinode_x < len(grid[0]):
                        antinodes.add((antinode_y, antinode_x))
                        antinode_y += y_distance
                        antinode_x += x_distance

                # opposite direction
                y_distance = - coord[0] - antenna[0]
                x_distance = - coord[1] - antenna[1]
                if not y_distance == 0 and not x_distance == 0: # If this is NOT the same space that we started
                    antinode_y = coord[0]
                    antinode_x = coord[1]

                    # if in bounds
                    while antinode_y >= 0 and antinode_y < len(grid) and antinode_x >= 0 and antinode_x < len(grid[0]):
                        antinodes.add((antinode_y, antinode_x))
                        antinode_y += y_distance
                        antinode_x += x_distance

    # return len([anti for anti in antinodes if anti[0] > 0 and anti[1] > 0])
    return len(antinodes)


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    return [line.strip() for line in file_lines]


if __name__ == "__main__":
    main()