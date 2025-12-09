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

# too high 4601733120
def part2(filename):
    coords = read_file(filename)

    areas = []
    for point in coords:
        for other_point in coords:
            if is_rect_inside_perimeter(point, other_point, coords):
                areas.append(find_rect_area_of_two_points(point, other_point))

    return max(areas)


def find_rect_area_of_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


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
        if not is_point_inside_perimeter_two(corner, perimeter):
            return False

    return True


def is_point_inside_perimeter(point, perimeter):
    x, y = point
    intersections = 0
    for i in range(len(perimeter)):
        p1 = perimeter[i]
        p2 = perimeter[(i+1) % len(perimeter)]
        
        # Check if point is on the edge
        if p1[1] == p2[1]:  # horizontal line
            if y == p1[1] and min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]):
                return True
        elif p1[0] == p2[0]:  # vertical line
            if x == p1[0] and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                return True
        
        # Ray casting - count intersections with edges crossing the ray
        y1, y2 = p1[1], p2[1]
        x1, x2 = p1[0], p2[0]
        
        if y1 > y2:
            y1, y2, x1, x2 = y2, y1, x2, x1
        
        # Check if ray at y intersects with edge
        if y1 < y <= y2:
            x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_intersect:
                intersections += 1
    
    return intersections % 2 == 1


def is_point_inside_perimeter_two(point, perimeter):
    """
    Check if a point is inside or on the perimeter formed by red tiles.
    The perimeter includes:
    - The red tiles themselves
    - Green tiles on straight lines between consecutive red tiles
    - Green tiles inside the closed loop
    """
    x, y = point
    
    # First check if point is on a red tile
    if point in perimeter:
        return True
    
    # Check if point is on a green tile (on the edge between consecutive red tiles)
    for i in range(len(perimeter)):
        p1 = perimeter[i]
        p2 = perimeter[(i + 1) % len(perimeter)]
        
        # Check if point lies on the line segment between p1 and p2
        if p1[0] == p2[0]:  # Vertical line
            if x == p1[0] and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                return True
        elif p1[1] == p2[1]:  # Horizontal line
            if y == p1[1] and min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]):
                return True
    
    # Use ray casting to check if point is inside the polygon
    # Cast a ray from point to the right and count intersections
    count = 0
    n = len(perimeter)
    
    for i in range(n):
        p1 = perimeter[i]
        p2 = perimeter[(i + 1) % n]
        
        y1, y2 = p1[1], p2[1]
        x1, x2 = p1[0], p2[0]
        
        # Check if the edge crosses the horizontal ray from point
        if min(y1, y2) < y <= max(y1, y2):
            # Calculate x coordinate of intersection
            if y1 != y2:  # Avoid division by zero
                x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < x_intersect:
                    count += 1
    
    # Point is inside if count is odd
    return count % 2 == 1


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [tuple([int(y) for y in x.strip().split(',')]) for x in data]


if __name__ == "__main__":
    main()