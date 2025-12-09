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

    #TODO: Maybe has something to do with that I'm parsing y,x instead of x,y?

    areas = []
    for point in coords:
        for other_point in coords:
            if all_points_inside_perimeter(point, other_point, coords):
                areas.append(find_rect_area_of_two_points(point, other_point))

    # return the largest area found
    return max(areas)



def find_rect_area_of_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def find_perimeter(coords):
    stack = []

    # Find lowest y point
    lowest_point = min(coords, key=lambda x: x[1])
    stack.append(lowest_point)
    coords.remove(lowest_point)

    # find angle from this point to all other points
    coords = sorted(coords, key=lambda c: math.atan2(c[1] - lowest_point[1], c[0] - lowest_point[0]))

    # for each point, determine if it makes a left or right turn
    for point in coords:
        while len(stack) >= 2:
            p2 = stack[-1]
            p1 = stack[-2]
            cross_product = (p2[0] - p1[0]) * (point[1] - p1[1]) - (p2[1] - p1[1]) * (point[0] - p1[0])
            if cross_product > 0:
                break
            else:
                stack.pop()
        stack.append(point)
    
    return stack


def print_grid(coords):
    max_x = max(x for x, _ in coords) + 1
    max_y = max(y for _, y in coords) + 1

    grid = [['.' for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1)]

    for x, y in coords:
        grid[y - 0][x - 0] = '#'

    for row in grid:
        print(''.join(row))

    

def all_points_inside_perimeter(p1, p2, coords):
    x1, y1 = p1
    x2, y2 = p2

    # Get rectangle corners
    rect_corners = [
        (min(x1, x2), min(y1, y2)),
        (min(x1, x2), max(y1, y2)),
        (max(x1, x2), min(y1, y2)),
        (max(x1, x2), max(y1, y2)),
    ]

    # Check if all corners are inside the perimeter
    for corner in rect_corners:
        if not is_point_inside_polygon(corner, coords):
            return False

    return True


# TODO: Fixme to be more simple.
def is_point_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside



# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [tuple([int(y) for y in x.strip().split(',')]) for x in data]


if __name__ == "__main__":
    main()