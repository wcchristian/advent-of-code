import os

_filename = "input.txt"

def main():
    print("\nDay 11: Dumbo Octopus")
    print("==============================")
    octopus_map_p1 = load_data()
    octopus_map_p2 = load_data()
    flash_count = process_steps(octopus_map_p1, 100)

    print(f"\nThe number of flashes is: {flash_count}")

    first_sync_flash_step = find_first_sync_flash(octopus_map_p2)

    print(f"\nThe first sync flash is at step: {first_sync_flash_step}")


def find_first_sync_flash(octopus_map):
    step = 0
    keep_going = True
    while keep_going:
        step += 1
        octopus_map, flashed = process_step(octopus_map)
        if check_for_sync_flash(octopus_map):
            return step



def process_steps(octopus_map, steps):
    flash_count = 0
    for step_idx in range(steps):
        octopus_map, flashed = process_step(octopus_map)
        flash_count += len(flashed)

    return flash_count


def check_for_sync_flash(octopus_map):
    result = True
    for line in octopus_map:
        for octopus in line:
            if octopus != 0:
                result = False
                break
    return result


def process_step(octopus_map):
    for y in range(len(octopus_map)):
        for x in range(len(octopus_map[y])):
            octopus_map[y][x] += 1

    flashed = []
    for y in range(len(octopus_map)):
        for x in range(len(octopus_map[y])):
            if octopus_map[y][x] > 9 and (y, x) not in flashed:
                octopus_map, flashed = flash(octopus_map, y, x, flashed)

    for y in range(len(octopus_map)):
        for x in range(len(octopus_map[0])):
            if octopus_map[y][x] > 9: octopus_map[y][x] = 0

    return octopus_map, flashed


def flash(octopus_map, y, x, flashed):
    flashed.append((y, x))
    neighbors = get_neighbors(octopus_map, y, x)

    for neighbor in neighbors:
        # power up
        n_y, n_x = neighbor
        octopus_map[n_y][n_x] += 1
        if octopus_map[n_y][n_x] > 9 and neighbor not in flashed:
            flash(octopus_map, n_y, n_x, flashed)


    return octopus_map, flashed


def get_neighbors(octopus_map, y, x):
    neighbors = []
    max_height_idx = len(octopus_map) - 1
    max_length_idx = len(octopus_map[0]) - 1

    # up
    if y - 1 >= 0: neighbors.append((y-1, x))
    # down
    if y + 1 <= max_height_idx: neighbors.append((y+1, x))
    # left
    if x - 1 >= 0: neighbors.append((y, x-1))
    # right
    if x + 1 <= max_length_idx: neighbors.append((y, x+1))
    # up left
    if y - 1 >= 0 and x - 1 >= 0: neighbors.append((y-1, x-1))
    # up right
    if y - 1 >= 0 and x + 1 <= max_length_idx: neighbors.append((y-1, x+1))
    # down left
    if y + 1 <= max_height_idx and x - 1 >= 0: neighbors.append((y+1, x-1))
    # down right
    if y + 1 <= max_height_idx and x + 1 <= max_length_idx: neighbors.append((y+1, x+1))

    return neighbors




def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    return [[int(y) for y in x.strip()] for x in lines]


if __name__ == "__main__":
    main()