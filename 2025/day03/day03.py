from pathlib import Path


def main():
    filename = "day03_input.txt"
    example_filename = "day03_example.txt"

    # print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')


def part1(filename):
    banks = read_file(filename)
    numbers = []

    for bank in banks:
        largest_number = -1
        largest_number_index = -1
        second_number = -1

        for i in range(len(bank)-1):
            cell = bank[i]
            if int(cell) > largest_number:
                largest_number = int(cell)
                largest_number_index = i

        for cell in bank[largest_number_index+1:]:
            if int(cell) > second_number:
                second_number = int(cell)

        numbers.append(int(str(largest_number) + str(second_number)))

    return sum(numbers)


def part2(filename):
    banks = read_file(filename)
    numbers = []

    for bank in banks:
        last_index = -1
        max_cells = 12
        search_window_width = len(bank) - max_cells + 1
        cells = [-1 for i in range(max_cells)]

        for i in range(0, max_cells):
            min_index = last_index + 1 # Start 1 after the last found index we are using
            numbers_left_to_find = cells.count(-1)
            possible_numbers_left = len(bank) - min_index
            max_index = min(min_index + search_window_width, (possible_numbers_left - numbers_left_to_find) + min_index) # min is to ensure we don't go out of bounds, otherwise

            if(numbers_left_to_find >= possible_numbers_left):
                for num in bank[min_index:]:
                    cells[cells.index(-1)] = int(num)
                break


            for j in range(min_index, max_index+1):
                cell = int(bank[j])
                if cell > cells[i]:
                    cells[i] = cell
                    last_index = j

        numbers.append(int(''.join(str(cell) for cell in cells)))
    return sum(numbers)


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return data


if __name__ == "__main__":
    main()