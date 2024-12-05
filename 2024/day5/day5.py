import os
import math

def main():
    filename = "day5_input.txt"
    example_filename = "day5_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    ordering_tuples, updates = read_input(filename)
    valid_updates, _ = check_update_validity(ordering_tuples, updates)
    return sum_middle_number_of_update_list(valid_updates)


def part2(filename):
    ordering_tuples, updates = read_input(filename)
    _, invalid_updates = check_update_validity(ordering_tuples, updates)
    ordered_updates = order_updates(ordering_tuples, invalid_updates)
    return sum_middle_number_of_update_list(ordered_updates)

def check_update_validity(ordering_tuples, updates):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if is_update_valid(ordering_tuples, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates

def sum_middle_number_of_update_list(updates):
    sum_of_middle_number = 0
    for update in updates:
        if len(update) % 2 == 1:
            mid_index = math.ceil(len(update) / 2) - 1
            sum_of_middle_number += update[mid_index]

    return sum_of_middle_number

def is_update_valid(ordering_tuples, update):
    for rule in ordering_tuples:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False

    return True

def order_updates(ordering_tuples, updates):

    fixed_updates = []
    for update in updates:
        fixed_updates.append(fix_update(ordering_tuples, update))

    return fixed_updates


def fix_update(ordering_tuples, update):
    if is_update_valid(ordering_tuples, update):
        return update
    else:
        shifted_update = update.copy()
        for page_idx in range(len(update)):
            for rule in ordering_tuples:
                if (rule[0] in update and rule[1] in update) and (update.index(rule[0]) > update.index(rule[1])):
                    del shifted_update[update.index(rule[0])]
                    shifted_update.insert(update.index(rule[1]), rule[0])
                    return fix_update(ordering_tuples, shifted_update)
        return shifted_update


def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_text = file.read()
    text_split = file_text.split("\n\n")
    ordering_lines = text_split[0].split("\n")
    update_lines = text_split[1].split("\n")

    ordering_tuples = []
    for line in ordering_lines:
        line_split = line.split("|")
        ordering_tuples.append((int(line_split[0]), int(line_split[1])))

    updates = []
    for line in update_lines:
        updates.append([int(x) for x in line.split(",")])

    return ordering_tuples, updates


if __name__ == "__main__":
    main()