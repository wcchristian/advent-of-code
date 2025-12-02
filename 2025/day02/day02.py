from pathlib import Path


def main():
    filename = "day02_input.txt"
    example_filename = "day02_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    ranges = read_file(filename)
    invalid_ids = []
    
    for r in ranges:
        min  = r.split('-')[0]
        max  = r.split('-')[1]

        for id in range(int(min), int(max)+1):
            if is_invalid_id(str(id)):
                invalid_ids.append(id)

    return sum([int(id) for id in invalid_ids])


def part2(filename):
    ranges = read_file(filename)
    invalid_ids = []
    
    for r in ranges:
        min  = r.split('-')[0]
        max  = r.split('-')[1]

        for id in range(int(min), int(max)+1):
            if is_invalid_id(str(id), is_part_2=True):
                invalid_ids.append(id)

    return sum([int(id) for id in invalid_ids])


def is_invalid_id(id: str, is_part_2: bool = False):
    length = len(id)
    is_even = length % 2 == 0

    if id[0] == "0":
        return True

    if is_even and id[:length//2] == id[length//2:]:
        return True

    # Basic idea here is to loop through substring lengths from 1 to half of the length of the id
    # since theoretically that would be the max sized substring that could repeat.
    # then split the id into parts of that length and check if all of the parts are the same. If so, we have a
    # repeating pattern and know that it's invalid.
    if is_part_2:
        for i in range(1, length//2 + 1) :
            parts_list = []

            for j in range(0, length, i):
                parts_list.append(id[j:j+i])

            if parts_list.count(parts_list[0]) == len(parts_list):
                return True
    
    return False


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip()
        data = data.split(',')

    return data


if __name__ == "__main__":
    main()
