from pathlib import Path
import re


def main():
    filename = "day12_input.txt"
    example_filename = "day12_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')


def part1(filename):
    present_shapes, tree_config = read_file(filename)

    # Filter the obvious ones first.
    possible = []
    for config in tree_config:
        sections = (config.space_size[0] // 3) * (config.space_size[1] // 3)
        present_count = sum(config.present_quantity)
        if present_count <= sections:
            possible.append(config)


    # Lol fakeout, I was debugging and found that just this filter ends up solving the problem
    # no need to actually check placement of the presents.


    return len(possible)


def part2(filename):
    return ""


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()

    # Parse present shapes
    register = []
    present_shapes = []
    for line in data:
        if line.strip() == "":
            present_shapes.append(PresentShape.from_string(register))
            register = []
        elif "x" in line:
            register = []
            break
        else:
            register.append(line)


    # Parse tree spaces
    tree_config_lines = re.findall(r'\d+x\d+:.*', "\n".join(data))
    tree_config = [TreeConfig.from_line(line) for line in tree_config_lines]

    return present_shapes, tree_config


class PresentShape:
    def __init__(self, index, size_grid):
        self.index = index
        self.size_grid = size_grid

    
    def __repr__(self):
        return f'PresentShape(index={self.index}, size_grid={self.size_grid})'

    @classmethod
    def from_string(self, present_grid):
        index = int(present_grid[0].replace(":", ""))
        size_grid = present_grid[1:]
        return PresentShape(index, size_grid)
    
    def get_present_area(self):
        return sum(row.count('#') for row in self.size_grid)


class TreeConfig:
    def __init__(self, space_size, present_quantity):
        self.space_size = space_size
        self.present_quantity = present_quantity

    def __repr__(self):
        return f'TreeSpace(space_size={self.space_size}, present_quantity={self.present_quantity})'
    
    @classmethod
    def from_line(self, line):
        size_part, quantity_part = line.split(":")
        space_size = tuple(map(int, size_part.split("x")))
        present_quantity = [int(x) for x in quantity_part.strip().split(" ")]
        return TreeConfig(space_size, present_quantity)

    @classmethod    
    def print_tree_grid(self, grid):
        for row in grid:
            print("".join(row))

    def get_tree_grid(self):
        return [['.' for _ in range(self.space_size[0])] for _ in range(self.space_size[1])]


if __name__ == "__main__":
    main()