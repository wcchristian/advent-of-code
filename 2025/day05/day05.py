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

def part2(filename):
    ranges, _ = read_file(filename)
    return count_ranges(ranges)


def count_ranges(ranges):
    count = 0
    max_number = 0
    sorted_ranges = sorted(ranges, key = lambda x: x[0])

    for r in sorted_ranges:
        if r[0] <= max_number and r[1] >= max_number:
            count += r[1] - max_number
            max_number = r[1]
        elif  r[0] > max_number:
            count += r[1] - r[0] + 1
            max_number = r[1]


    return count


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