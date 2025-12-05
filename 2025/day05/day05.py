from pathlib import Path


def main():
    filename = "day05_input.txt"
    example_filename = "day05_example.txt"

    #print(f'Part 1 Example: {part1(example_filename)}')
    #print(f'Part 1: {part1(filename)}')
    #print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    ranges, ingredients = read_file(filename)

    fresh_count = 0
    for ingredient in ingredients:
        fresh_count += 1 if is_in_range(ingredient, ranges) else 0

    return fresh_count

# 868333791996222 too high
def part2(filename):
    ranges, _ = read_file(filename)
    sorted(ranges, key=lambda x: x[0])
    filtered_ranges = [ranges[0]]

    # Consolidate ranges
    filtered_ranges = consolodate_range_list(ranges)

    # Add up numbers in the range.
    total = 0
    for r in filtered_ranges:
        total += r[1] - r[0] + 1

    return total


def consolodate_range_list(ranges):
    filtered_ranges = [ranges[0]]
    mod_count = 0

    for a, b in ranges:
        append_new = True
        for i in range(len(filtered_ranges)):
            x, y = filtered_ranges[i]

            # if both within, break
            if a >= x and b <= y:
                append_new = False
                break
            #TODO, should I break this into multiple statements to be more explicit, should probablyt compare this against all cases we could see.
            elif (a >= x and a < y) or (b <= y and b < x): # inbound to some degree
                filtered_ranges[i] = (min(a, x), max(b, y))
                append_new = False
                mod_count += 1
                break

        if append_new:
            filtered_ranges.append((a, b))

    if mod_count > 0:
        return consolodate_range_list(filtered_ranges)
    else:
        return filtered_ranges


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