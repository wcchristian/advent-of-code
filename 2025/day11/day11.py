from pathlib import Path
from functools import cache

device_dict = None

def main():
    filename = "day11_input.txt"
    example_filename = "day11_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2("day11p2_example.txt")}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    global device_dict
    device_dict = read_file(filename)
    count.cache_clear()
    return count('you', 'out')


def part2(filename):
    global device_dict
    device_dict = read_file(filename)
    count.cache_clear()

    p2  = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    p2 += count("svr", "dac") * count("dac", "fft") * count("fft", "out")

    return p2


@cache
def count(start, end):
    if start == end:
        return 1
    else:
        next = [count(next, end) for next in device_dict.get(start, [])]
        return sum(next)


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()


    device_dict = {}
    for line in data:
        line_split = line.strip().split(':')
        device = line_split[0]
        outputs = line_split[1].strip().split(' ')
        device_dict[device] = outputs


    return device_dict


if __name__ == "__main__":
    main()