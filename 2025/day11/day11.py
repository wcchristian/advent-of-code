from pathlib import Path


def main():
    filename = "day11_input.txt"
    example_filename = "day11_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2("day11p2_example.txt")}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    device_dict = read_file(filename)
    return count_paths(device_dict, 'you')


def part2(filename):
    device_dict = read_file(filename)
    #NOTE: This line will explode your memory paths = collect_paths(device_dict, 'svr')
    return count_paths2(device_dict, 'svr', req_devices={'dac': False, 'fft': False})


# Initially tried to cache like the beam splitting problem but in this case since there are cycles
# that would end up not counting all paths, just the first one it found for a node.
# Funnily enough that was giving me the same answer as the example part 1.
def count_paths(device_dict, current_device):
    if current_device == 'out':
        return 1

    total_paths = 0
    outputs = device_dict[current_device]
    for output in outputs:
        total_paths += count_paths(device_dict, output)

    return total_paths


def collect_paths(device_dict, current_device, current_path=[], paths=[]):
    current_path.append(current_device)

    if current_device == 'out':
        paths.append(current_path)
        current_path = []
        return paths

    outputs = device_dict[current_device]
    for output in outputs:
        paths.extend(collect_paths(device_dict, output, current_path, paths))

    return paths


def count_paths2(device_dict, current_device, req_devices=None):

    if req_devices and current_device in req_devices.keys():
        req_devices[current_device] = True

    if current_device == 'out':
        return 1 if all(list(req_devices.values())) else 0

    total_paths = 0
    outputs = device_dict[current_device]
    for output in outputs:
        total_paths += count_paths2(device_dict, output, req_devices)

    return total_paths


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()


    device_dict = {}
    for line in data:
        line_split = line.strip().split(':')
        device = line_split[0]
        outputs = line_split[1].strip().split(' ')
        device_dict[device] = outputs


    return device_dict



if __name__ == "__main__":
    main()