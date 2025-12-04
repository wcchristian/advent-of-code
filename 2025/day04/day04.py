from pathlib import Path
import copy


def main():
    filename = "day04_input.txt"
    example_filename = "day04_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename: str):
    grid = read_file(filename)
    forkliftable = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == "@"):
                neighbors = find_neighbors(y, x, grid)

                if list(neighbors.values()).count("@") < 4:
                    forkliftable.append((y, x))

    return len(forkliftable)


def part2(filename: str):
    grid = read_file(filename)

    new_grid = move_tp(grid, True)

    moved_count = 0
    for line in new_grid:
        for c in line:
            if c == "x":
                moved_count += 1

    return moved_count


def move_tp(grid, recur = False):
    forkliftable = []
    new_grid = copy.deepcopy(grid)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == "@"):
                neighbors = find_neighbors(y, x, grid)

                if list(neighbors.values()).count("@") < 4:
                    new_grid[y][x] = 'x'
                    forkliftable.append((y, x))


    if len(forkliftable) <= 0:
        return new_grid
    elif recur:
        return move_tp(new_grid, True)
    else:
        return new_grid


def find_neighbors(y: int, x: int, grid):
    directions = [
        (-1, 0), # n
        (-1, 1), # ne
        (0, 1),  # e
        (1, 1),  # se
        (1, 0),  # s
        (1, -1), # sw
        (0, -1), # w
        (-1, -1) # nw
    ]

    neighbors = {}

    for direction in directions:
        try:
            new_y = y + direction[0]
            new_x = x + direction[1]
            if new_y >= 0 and new_x >= 0:
                neighbors[new_y, new_x] = grid[new_y][new_x]
        except IndexError:
            pass


    return neighbors


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [list(x) for x in data]


if __name__ == "__main__":
    main()
