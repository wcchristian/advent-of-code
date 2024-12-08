import os

def main():
    filename = "day8_input.txt"
    example_filename = "day8_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)
    antinodes = set()
    antenna_dict = dict()

    # Find the coords of all antennas, dictionary of frequency: [points]?
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x].isalnum():
                antenna_dict[grid[y][x]] = (y, x)


    # For each antenna
        # for each other antenna at this frequency
            # where would the point be? #MATH
            # add this point to our set of possible antinodes.


        # find it's compliments in the list of points.
        # add the antinode to the list of possible antinodes IF it can be located on the grid

    # Loop through the grid
        # if point is an antinode
            # Add to set?


    # return count of length of the set

    return len(antinodes)


def part2(filename):
    lines = read_input(filename)

    return 0


def is_antinode(coord, grid):
    # Check in each direction until you fin
    return


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    return [line.strip() for line in file_lines]


if __name__ == "__main__":
    main()