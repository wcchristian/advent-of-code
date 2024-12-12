import os
import re
from tqdm import tqdm

def main():
    filename = "day9_input.txt"
    example_filename = "day9_example.txt"

    # print(f'Part 1 Example: {part1(example_filename)}')
    # print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2_2(example_filename)}')
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
    current_id_to_move = max_id

    for i in tqdm(range(len(visual_list))):
        if visual_list[i] == '.':

            # find how many spaces I have
            num_dot_spaces = 0
            for j in range(len(visual_list[i:])):
                if visual_list[i:][j] != '.':
                    break
                num_dot_spaces += 1

            # Probably need to loop this over the end until I reach the number I'm
            # currently at??
            for x in reversed(range(0, current_id_to_move+1)):
                # find the left most chunk that can fit there
                starting_idx = visual_list.index(str(x))
                if starting_idx <= i:
                    break
                num_num_spaces = 0
                for j in range(len(visual_list[starting_idx:])):
                    if visual_list[starting_idx:][j] != str(x):
                        break
                    num_num_spaces += 1

                if(num_dot_spaces >= num_num_spaces):
                    for j in range(i, i+num_dot_spaces):
                        visual_list[j] = x
                    for j in range(starting_idx, starting_idx+num_num_spaces):
                        visual_list[j] = "."
                current_id_to_move -= 1

    return calc_checksum(visual_list) 


def part2_2(filename):
    line = read_input(filename)
    visual_list = "".join(translate_line_to_visual_list(line)[0])
    dot_array = [x for x in re.split(r'\d', visual_list) if x != '']
    numarray = "".join([x for x in re.split(r'\.', visual_list) if x != ''])


    num_array = []
    current_string = ''
    current_digit = '0'
    for i in range(len(numarray)):
        if(current_digit != numarray[i]):
            num_array.append(current_string)
            current_digit = numarray[i]
            current_string = ''
        current_string += numarray[i]
    num_array.append(current_string)



    for i in range(len(dot_array)):
        for j in reversed(range(len(num_array))):
            left_over = len("".join([x for x in re.split(r'\d', dot_array[i]) if x != ''])) - len(num_array[j])
            if left_over >= 0 and len([x for x in dot_array[i].split(".")]) == 0:
                dot_array[i] = num_array[j] + ('.' * left_over)
            elif left_over >= 0:
                index_where_dots_start = dot_array.index(".")
                dot_array[i] = dot_array[i][:index_where_dots_start] + num_array[j] + ('.' * left_over)




    print("foo")


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