from pathlib import Path
from math import floor

def main():
    filename = "day01_input.txt"
    example_filename = "day01_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    lines = read_file(filename)
    position = 50
    counter = 0 

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            position += distance
        elif direction == "L":
            position -= distance

        position = position % 100

        if position == 0:
            counter += 1

    return counter


# Feel like I could make this part better.
def part2(filename):
    position = 50
    counter = 0 
    lines = read_file(filename)

    for line in lines:
        starting_pos = position
        direction = line[0]
        full_distance = int(line[1:])
        distance = full_distance % 100
        counter += floor(full_distance / 100)

        if direction == "R" and position + distance > 99:
            position = (position + distance) - 100
            counter += 1 if starting_pos != 0 else 0
        elif direction == "R":
            position += distance
            counter += 1 if position == 0 else 0
        elif direction == "L" and position - distance < 0:
            position = (100 - abs(position - distance))
            counter +=  1 if starting_pos != 0 else 0
        elif direction == "L":
            position -= distance
            counter += 1 if position == 0 else 0

    return counter



# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return data

if __name__ == "__main__":
    main()

    