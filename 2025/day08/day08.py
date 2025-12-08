from cmath import sqrt
from pathlib import Path


def main():
    filename = "day08_input.txt"
    example_filename = "day08_example.txt"

    print(f'Part 1 Example: {part1(example_filename, 10)}')
    print(f'Part 1: {part1(filename, 1000)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')

def part1(filename, num_iterations=10):
    # Build my list of each point combination with their distances.
    coords = read_file(filename)
    point_distances = build_point_distances(coords)

    circuits = []
    for _ in range(num_iterations):
        circuits, _ = find_next_closest_points(point_distances, circuits)

    circuits = list(reversed(sorted(circuits, key=lambda x: len(x))))
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part2(filename):
    # Build my list of each point combination with their distances.
    coords = read_file(filename)
    point_distances = build_point_distances(coords)

    # Iterate until all points are in a circuit.
    circuits = []
    for _ in range(len(point_distances)):
        circuits, last_connection = find_next_closest_points(point_distances, circuits)

        if len(circuits) == 1 and len(circuits[0]) == len(coords):
            break

    return last_connection[0][0] * last_connection[1][0]


def find_next_closest_points(point_distances, circuits):
        # take the smallest distance, connect to circuit
        smallest_pd = point_distances.pop(0)
        point1 = smallest_pd.point1
        point2 = smallest_pd.point2

        # find if either point is already in a circuit
        circuit1 = next((c for c in circuits if point1 in c), None)
        circuit2 = next((c for c in circuits if point2 in c), None)

        # Merge or add points, create circuits as needed
        if circuit1 and circuit2:
            if circuit1 != circuit2:
                # merge circuits
                circuit1.extend(circuit2)
                circuits.remove(circuit2)
        elif circuit1:
            circuit1.append(point2)
        elif circuit2:
            circuit2.append(point1)
        else:
            circuits.append([point1, point2])

        return circuits, (point1, point2)


def build_point_distances(coords):
    point_distances = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = calculate_distance(coords[i], coords[j])
            pd = PointDistance(coords[i], coords[j], distance)
            point_distances.append(pd)

    point_distances = sorted(point_distances, key=lambda x: x.distance)
    return point_distances


def calculate_distance(p1, p2):
    # https://en.wikipedia.org/wiki/Euclidean_distance
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2).real


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return [tuple([int(y) for y in x.strip().split(',')]) for x in data]


class PointDistance:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


if __name__ == "__main__":
    main()