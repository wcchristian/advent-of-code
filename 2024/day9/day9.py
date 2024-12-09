import os

def main():
    filename = "day9_input.txt"
    example_filename = "day9_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    # print(f'Part 2 Example: {part2(example_filename)}')
    # print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    line = read_input(filename)
    newString = translate_line_to_visual_format(line)

    return 0


def part2(filename):
    lines = read_input(filename)

    return 0


def translate_line_to_visual_format(line):
    result_string = ""
    is_block = True
    current_id = 0
    for i in range(len(line)):
        if is_block:
            for j in range(int(line[i])):
                result_string += str(current_id)
            current_id += 1
        else:
            for j in range(int(line[i])):
                result_string += "."

        is_block = not is_block


    return result_string


def defragment(line):
    # move through the list
    # for each ., find the last thing in the list and move it here
    # move the dot to the end.
    backwards_line = line.r
    current_id = line.reversed().index()
    for i in range(len(line)):
        if not line[i].isalnum():
            # look at the line backwards to find the 
            backwards_line = line.reverse()
            index_of_last_item = backwards_line.index()
        


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    line = file.read()

    return line


if __name__ == "__main__":
    main()