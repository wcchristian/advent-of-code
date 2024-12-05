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

def main():
    filename = "day4_input.txt"
    example_filename = "day4_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    grid = read_input(filename)

    # Find X
    counter = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                counter += depth_first_search_for_christmas((y, x), grid) #TODO: Switch around x and y?

    # Process X

    return counter


def part2(filename):
    lines = read_input(filename)

    return 0

def depth_first_search_for_christmas(coord, grid):

    # Find all of the neighbors that match (CHECK BOUNDS OF THE ARRAY, IF WE HIT A WALL, WE ARE DONE)
    counter = 0
    for neighbor in neighbor_direction_tuple_map:
        direction = None
        new_coords = (coord[0] + neighbor_direction_tuple_map[neighbor][0], coord[1] + neighbor_direction_tuple_map[neighbor][1])
        are_new_coords_out_of_range = new_coords[0] < 0 or new_coords[0] >= len(grid) or new_coords[1] < 0 or new_coords[1] >= len(grid[0])
        if not are_new_coords_out_of_range and grid[new_coords[0]][new_coords[1]] == 'M':
            print("Found M")
            counter += 1

        # Check to see if neighbor is valid, if it IS, set direction and check to the end. If success, increment counter.

        print(neighbor)

    # For each "correct" neighbor, check in it's direction until you find 's" or not

    # IF you do find "S" break true, else break false



    return counter

def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    word_search_grid = file.readlines()

    return word_search_grid


if __name__ == "__main__":
    main()