from operator import contains
import os
import re
from tqdm import tqdm

def main():
    filename = "day9_input.txt"
    example_filename = "day9_example.txt"

    # print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2_2(filename)}')
    

def part1(filename):
    line = read_input(filename)
    visual_list, max_id = translate_line_to_visual_list(line)
    current_id_to_move = max_id
    count_of_current_id_to_move = len([x for x in visual_list if x == str(current_id_to_move)])

    for i in tqdm(range(len(visual_list))):
        if visual_list[i] == '.':

            # decrement our id counter
            if(count_of_current_id_to_move == 0):
                current_id_to_move -= 1
                count_of_current_id_to_move = len([x for x in visual_list if x == str(current_id_to_move)]) - 1 # -1 because we are placing one right now
            else:
                count_of_current_id_to_move -= 1


            # Move the id to the . location
            visual_list[i] = str(current_id_to_move)

            # Move the . to the id location
            copied_list = visual_list.copy()
            copied_list.reverse()
            offset = copied_list.index(str(current_id_to_move))
            visual_list[len(visual_list) - offset - 1] = '.'


    return calc_checksum(visual_list)  


def part2(filename):
    line = read_input(filename)
    visual_list, max_id = translate_line_to_visual_list(line)
    chunked_list = visual_list_to_chunked_list(visual_list)
    current_id_to_move = max_id

    for source_chunk in reversed(chunked_list):
        dot_chunks = [x for x in chunked_list if re.match(r"\.*", x)]

        #TODO: I think this process will work. But there is a problem below
        # when I try and assign things back to the string because "Strings don;t
        # Support Item Assignment."

        # If chunk is numbers only. (IF IS A FILE)
        for destination_chunk in chunked_list:
            # check if the destination_chunk contains dots.
            if re.match(r"\.*", destination_chunk):
                # count the dots
                dot_count = len (re.findall(r"\.", destination_chunk))

                # If it has room for the source_chunk
                if len(source_chunk) <= dot_count:
                    dot_start_index = destination_chunk.index('.')
                    for x in range(dot_start_index, dot_count + dot_start_index + 1):
                        destination_chunk[x] = source_chunk[x - (dot_start_index)]
                        source_chunk[x - (dot_start_index)] = "."

    return calc_checksum(visual_list) 


def calc_checksum(list):
    sum = 0
    for i in range(len(list)):
        if list[i] != '.':
            sum += i * int(list[i])
    return sum


def translate_line_to_visual_list(line):
    result_list = []
    is_block = True
    current_id = 0
    for i in range(len(line)):
        if is_block:
            for j in range(int(line[i])):
                result_list.append(str(current_id))
            current_id += 1
        else:
            for j in range(int(line[i])):
                result_list.append(".")

        is_block = not is_block


    return result_list, current_id - 1

def visual_list_to_chunked_list(visual_list):
    chunked_list = []
    tmp_str = ""
    prev_char = visual_list[0]
    for char in visual_list[1:]:
        if prev_char == char and (len(tmp_str) == 0 or tmp_str[0] == char):
            tmp_str += char
        else:
            chunked_list.append(tmp_str)
            prev_char = char
            tmp_str = "" + char

    chunked_list.append(tmp_str)
    return chunked_list


def replace_fragment(line, fragment, index_to_replace):
    line_array = list(line)
    last_index =  line.rfind(fragment)
    first_index = last_index - (len(fragment) - 1)

    if first_index == last_index:
        line_array[first_index] = '.'
        line_array[index_to_replace] = fragment

    # # swap the things
    # for i in range(last_index - first_index):
    #     new_string[i] = fragment[i]
    #     new_string[first_index + i] = '.'

    return "".join(line_array)


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    line = file.read()

    return line


if __name__ == "__main__":
    main()