from pathlib import Path


def main():
    filename = "day05_input.txt"
    example_filename = "day05_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    ranges, ingredients = read_file(filename)

    fresh_count = 0
    for ingredient in ingredients:
        fresh_count += 1 if is_in_range(ingredient, ranges) else 0

    return fresh_count

# 868333791996222 too high
# 322287238722640 is wrong
def part2(filename):
    ranges, _ = read_file(filename)

    # Consolidate ranges
    consolidated_ranges = consolidate_ranges(ranges)


    # sort ranges
    # loop up, if overlap, combine them


    # Add up numbers in the range.

    return sum([x[1] - x[0] + 1 for x in consolidate_ranges])

    total = 0
    for r in consolidated_ranges:
        total += r[1] - r[0] + 1

    return total


def consolidate_ranges(ranges):
    # sort
    sorted(ranges, key = lambda x: x[0])
    i = 0
    mods = 0
    while(i in range(len(ranges))):
        prev_range = ranges[i-1] if i > 0 else None
        current_range = ranges[i]

        if prev_range != None and current_range[0] <= prev_range[1]:
            ranges[i-1] = (prev_range[0], current_range[1])
            del ranges[i]
            mods += 1
            continue
        else:
            i += 1

    if mods == 0:
        return ranges
    else:
        return consolidate_ranges(ranges)

    print("What am I doing?")


        # check the prev range if applicable
        # if it's entirely out of bounds, move on
        # if it's in bounds merge this to the prev and continue.


def is_in_range(ingredient, ranges):
    for range in ranges:
        if ingredient <= range[1] and ingredient >= range[0]:
            return True

    return False


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip()

    data_split = data.split("\n\n")
    ranges = data_split[0].split("\n")
    ingredients = [int(x) for x in data_split[1].split("\n")]

    range_tuples = []
    for range in ranges:
        range_split = range.split("-")
        range_tuples.append((int(range_split[0]), int(range_split[1])))

    return range_tuples, ingredients


if __name__ == "__main__":
    main()