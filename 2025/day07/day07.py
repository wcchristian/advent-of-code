from pathlib import Path


def main():
    filename = "day07_input.txt"
    example_filename = "day07_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    grid = read_file(filename)
    starting_point = find_starting_point(grid)
    splits = count_splits(grid, starting_point, set())
    return len(splits)


def part2(filename):
    grid = read_file(filename)
    starting_point = find_starting_point(grid)
    timelines = count_timelines(grid, starting_point)
    return timelines


def find_starting_point(grid):
    for idx, char in enumerate(grid[0]):
        if char == "S":
            return (0, idx)


def count_splits(grid, point, split_set):
    # Move down the grid for the next split, recur on 
    while(point[0] < len(grid) - 1):
        point = (point[0]+1, point[1]) # Move down
        
        if(point in split_set):
            return split_set # Already counted from this point, skip it
        
        if (grid[point[0]][point[1]] == "^"): # If we need to split, spawn a new check to the left and the right of the splitter
            split_set.add(point)
            left = count_splits(grid, (point[0], point[1]-1), split_set)
            right = count_splits(grid, (point[0], point[1]+1), split_set)
            return split_set.union(left, right)

    return split_set


def count_timelines(grid, point, count = 0, cache={}):
    # Move down the grid for the next split, recur on 
    while(point[0] < len(grid) - 1):
        point = (point[0]+1, point[1]) # Move down
        
        if (grid[point[0]][point[1]] == "^"): # If we need to split, spawn a new check to the left and the right of the splitter

            # Check Left
            if (point[0], point[1]-1, count) in cache:
                left = cache[(point[0], point[1]-1, count)]
            else:
                left = count_timelines(grid, (point[0], point[1]-1), count, cache)
                cache[(point[0], point[1]-1, count)] = left


            # Check Right
            if (point[0], point[1]+1, count) in cache:
                right = cache[(point[0], point[1]+1, count)]
            else:
                right = count_timelines(grid, (point[0], point[1]+1), count, cache)
                cache[(point[0], point[1]+1, count)] = right

            return left + right

    count += 1
    return count


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [x for x in data]


if __name__ == "__main__":
    main()