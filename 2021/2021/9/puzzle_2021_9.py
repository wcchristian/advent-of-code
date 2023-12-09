import os

_filename = "input.txt"


def main():
    print("\nDay 9: Smoke Basin")
    print("==============================")

    height_map = load_data()
    padded_map = pad_map(height_map)
    low_points = find_low_points(padded_map)
    sum_of_risk_part_1 = calc_risk_sum(low_points, padded_map)

    print(f"\np1: The sum of risk is: {sum_of_risk_part_1}")

    basins = sorted(find_basin_sizes(low_points, padded_map))
    top_three = basins[len(basins)-3:]
    product_top_3 = top_three[0] * top_three[1] * top_three[2]

    print(f"\n\np2: The product of the 3 largest basins is: {product_top_3}")


def pad_map(height_map):

    for line in height_map:
        line.insert(0, -1)
        line.append(-1)

    pad_line = [-1 for x in range(len(height_map[0]))]
    height_map.insert(0, pad_line)
    height_map.append(pad_line)

    return height_map


def find_low_points(height_map):
    low_points = []
    for y in range(1, len(height_map)-1):
        for x in range(1, len(height_map[y])-1):
            current_point = height_map[y][x]
            neighbors = find_neighbors([x, y])
            smallest_space = min([height_map[x[1]][x[0]] for x in neighbors if height_map[x[1]][x[0]] != -1])

            if current_point < smallest_space:
                low_points.append([x, y])

    return low_points


def find_basin_sizes(low_points, padded_map):
    basin_list = []
    for point in low_points:
        basin_list.append(find_basin(point, padded_map))

    return [len(basin) for basin in basin_list]


def find_neighbors(position):
    x = position[0]
    y = position[1]
    return [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]


def find_basin(low_point, height_map):
    positions_to_try = [low_point]
    for current_position in positions_to_try:
        neighbors = find_neighbors(current_position)
        for neighbor in neighbors:
            if neighbor not in positions_to_try and height_map[neighbor[1]][neighbor[0]] < 9 and height_map[neighbor[1]][neighbor[0]] != -1:
                positions_to_try.append(neighbor)
    return positions_to_try


def calc_risk_sum(low_points, height_map):
    return sum([height_map[x[1]][x[0]] + 1 for x in low_points])


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    result_lines = []

    for line in lines:
        chars = list(line.strip())
        ints = [int(x) for x in chars]
        result_lines.append(ints)

    return result_lines


if __name__ == "__main__":
    main()