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

# previous attempt returned 4601733120 (too high)
def part2(filename):
    coords = read_file(filename)
    segments = build_perimeter_segments(coords)

    areas = []
    for point in coords:
        for other_point in coords:
            if is_rect_inside_perimeter(point, other_point, coords, segments):
                areas.append(find_rect_area_of_two_points(point, other_point))

    return max(areas)


def find_rect_area_of_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def is_rect_inside_perimeter(p1, p2, perimeter, segments):
    x1, y1 = p1
    x2, y2 = p2

    corners = [
        (x1, y1),
        (x1, y2),
        (x2, y1),
        (x2, y2)
    ]

    for corner in corners:
        if not is_point_inside_perimeter_two(corner, perimeter):
            return False

    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))

    # Reject rectangles whose vertical edges cross the loop.
    for y, low_x, high_x in segments["h"]:
        if min_y < y < max_y:
            if max(low_x, min_x) < min(high_x, max_x):
                return False

    # Reject rectangles whose horizontal edges cross the loop.
    for x, low_y, high_y in segments["v"]:
        if min_x < x < max_x:
            if max(low_y, min_y) < min(high_y, max_y):
                return False

    return True


def build_perimeter_segments(perimeter):
    horizontal = []
    vertical = []

    n = len(perimeter)
    for i in range(n):
        x1, y1 = perimeter[i]
        x2, y2 = perimeter[(i + 1) % n]

        if x1 == x2:
            low_y, high_y = sorted((y1, y2))
            vertical.append((x1, low_y, high_y))
        else:
            low_x, high_x = sorted((x1, x2))
            horizontal.append((y1, low_x, high_x))

    return {"h": horizontal, "v": vertical}


def is_point_inside_perimeter_two(point, perimeter):
    """Return True when the point is on or inside the red/green loop."""
    px, py = point

    red_tiles = set(perimeter)
    if point in red_tiles:
        return True

    intersections = 0
    n = len(perimeter)

    for i in range(n):
        x1, y1 = perimeter[i]
        x2, y2 = perimeter[(i + 1) % n]

        # The puzzle guarantees axis-aligned step segments.
        if x1 == x2:
            low_y, high_y = sorted((y1, y2))
            if px == x1 and low_y <= py <= high_y:
                return True
            if px < x1 and low_y <= py < high_y:
                intersections += 1
        elif y1 == y2:
            low_x, high_x = sorted((x1, x2))
            if py == y1 and low_x <= px <= high_x:
                return True

    return intersections % 2 == 1


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [tuple([int(y) for y in x.strip().split(',')]) for x in data]


if __name__ == "__main__":
    main()