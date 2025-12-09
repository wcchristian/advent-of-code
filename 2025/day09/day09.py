from pathlib import Path
import math

# using Graham scan algorithm to find perimeter of points
# using shoelace formula to find area of perimeter

def main():
    filename = "day09_input.txt"
    example_filename = "day09_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    coords = read_file(filename)

    areas = []
    for point in coords:
        for other_point in coords:
            areas.append(find_rect_area_of_two_points(point, other_point))

    return max(areas)

#TODO: Probably need to debug this point by point. Make sure that at each step my code is working properly.
def part2(filename):
    coords = read_file(filename)
    print_grid(coords)
    perimeter = build_perimeter(coords)

    # areas = []
    # for point in coords:
    #     for other_point in coords:
    #         if all_points_inside_perimeter(point, other_point, perimeter):
    #             areas.append(find_rect_area_of_two_points(point, other_point))

    # return max(areas)
    return 1



def find_rect_area_of_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def print_grid(coords):
    max_x = max(x for x, _ in coords) + 1
    max_y = max(y for _, y in coords) + 1

    grid = [['.' for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1)]

    for x, y in coords:
        grid[y - 0][x - 0] = '#'

    for row in grid:
        print(''.join(row))


def is_rect_inside_perimeter(p1, p2, perimeter):
    x1, y1 = p1
    x2, y2 = p2

    corners = [
        (x1, y1),
        (x1, y2),
        (x2, y1),
        (x2, y2)
    ]

    for corner in corners:
        if not is_point_inside_perimeter(corner, perimeter):
            return False

    return True


def is_point_inside_perimeter(point, perimeter):
    x, y = point
    inside = False

    n = len(perimeter)
    p1x, p1y = perimeter[0]
    for i in range(n + 1):
        p2x, p2y = perimeter[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def build_perimeter(coords):

    perimeter = []

    for i in range(len(coords)):
        p1 = coords[i]
        p2 = coords[i+1] if i < len(coords) - 1 else coords[0]

        x = p2[0] - p1[0]
        y = p2[1] - p1[1]

        if x != 0:
            step = 1 if x > 0 else -1
            for xi in range(p1[0], p2[0] + step, step):
                perimeter.append((xi, p1[1]))
        elif y != 0:
            step = 1 if y > 0 else -1
            for yi in range(p1[1], p2[1] + step, step):
                perimeter.append((p1[0], yi))

    return perimeter


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [tuple([int(y) for y in x.strip().split(',')]) for x in data]


if __name__ == "__main__":
    main()