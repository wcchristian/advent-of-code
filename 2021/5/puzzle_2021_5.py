import os
from PIL import Image

_filename = "input.txt"
_map_file = "map.txt"
_image_file = "image.png"

def main():
    coordinates = load_data()
    base_map = init_map(coordinates)
    vent_map = generate_vent_map(coordinates, base_map)
    overlap_count = count_overlap(vent_map)
    # draw_map(base_map) # Don't do this if the map is super large
    write_map_to_file(vent_map)
    draw_image(vent_map)

    print(f"{get_max_xy(coordinates)}")

    print(f"It overlapped {overlap_count} times")

def draw_image(vent_map):
    y_size = len(vent_map)
    x_size = len(vent_map[0])
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _image_file)

    img = Image.new("RGB", (x_size, y_size), color="black")
    pixels = img.load()

    for line_idx in range(y_size):
        for space_idx in range(x_size):
            color = (0, 0, 0)
            match vent_map[line_idx][space_idx]:
                case 1:
                    color = (0, 0, 255)
                case 2:
                    color = (0, 255, 0)
                case 3:
                    color= (255, 255, 0)
                case 4:
                    color = (255, 128, 0)
                case 5:
                    color = (255, 0, 0)
            
            pixels[space_idx, line_idx] = color
    img.save(filepath)



def count_overlap(vent_map):
    count=0
    for line in vent_map:
        for space in line:
            if space != '.' and int(space) > 1:
                count += 1
    return count


def init_map(coordinates):
    max_x_y = get_max_xy(coordinates)
    point_map = []
    for y in range(max_x_y[1]+1):
        x_map = []
        for x in range(max_x_y[0]+1):
            x_map.append('.')
        point_map.append(x_map)
    return point_map

def generate_vent_map(coordinates, map):
    for coord in coordinates:
        # if x == x, then movement is y
        if coord[0][0] == coord[1][0]:
            min_range = min(coord[0][1], coord[1][1])
            max_range = max(coord[0][1], coord[1][1])
            for i in range(min_range, max_range+1):
                if map[i][coord[0][0]] == '.':
                    map[i][coord[0][0]] = 1
                else: 
                    map[i][coord[0][0]] += 1

        elif coord[0][1] == coord[1][1]:
            print()
            min_range = min(coord[0][0], coord[1][0])
            max_range = max(coord[0][0], coord[1][0])
            for i in range(min_range, max_range+1):
                if map[coord[0][1]][i] == '.':
                    map[coord[0][1]][i] = 1
                else: 
                    map[coord[0][1]][i] += 1
        else: # They are diagonal
            x_movement = 0
            y_movement = 0
            if coord[0][0] >= coord[1][0]:
                x_movement = -1
            else:
                x_movement = 1

            if coord[0][1] >= coord[1][1]:
                y_movement = -1
            else:
                y_movement = 1

            x = coord[0][0]
            y = coord[0][1]
            dest_x = coord[1][0]
            dest_y = coord[1][1]
            while True:
                if map[y][x] == '.':
                    map[y][x] = 1
                else:
                    map[y][x] += 1
                map[y][x] 

                if x == dest_x and y == dest_y:
                    break

                x += x_movement
                y += y_movement

    return map


def draw_map(vent_map):
    for row in vent_map:
        for cell in row:
            print(str(cell) + " ", end='')
        print("\n", end='')

def write_map_to_file(vent_map):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _map_file)

    try:
        os.remove(filepath)
    except FileNotFoundError:
        print("Map File not found. Creating it...")

    with open(filepath, "w") as f:
        for row in vent_map:
            for cell in row:
                f.write(str(cell) + " ")
            f.write("\n")


def get_max_xy(coordinates):
    max_x = 0
    max_y = 0
    x_numbers = []
    y_numbers = []
    for coordinate in coordinates:
        x_numbers.append(coordinate[0][0])
        x_numbers.append(coordinate[1][0])
        y_numbers.append(coordinate[0][1])
        y_numbers.append(coordinate[1][1])

    max_x = max(x_numbers)
    max_y = max(y_numbers)

    return (max_x, max_y)



def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    coordinate_list = []
    for line in lines:
        line_split = line.split("->")
        source = line_split[0].strip().split(",")
        source_int = [int(x) for x in source]
        destination = line_split[1].strip().split(",")
        dest_int = [int(x) for x in destination]
        coordinates = [source_int, dest_int]
        coordinate_list.append(coordinates)
    
    return coordinate_list


if __name__ == "__main__":
    main()