import os

_filename = "input.txt"

def main():
    print("\nDay 8: Seven Segment Search")
    print("==============================")

    signal_array = load_data()

    unique_seg_count = process_data_count_unique_seg(signal_array)

    print(f"\np1: The count of numbers with unique segment counts is: {unique_seg_count}")

    result_sum = process_data_sum_results(signal_array)

    print(f"\np2: The sum of result numbers is: {result_sum}\n")


def process_data_sum_results(signal_array):
    result_sum = 0
    for signal_line in signal_array:
        signal_lookup = generate_signal_lookup(signal_line)
        result_sum += lookup_result(signal_line, signal_lookup)
    return result_sum
        
def process_data_count_unique_seg(signal_array):
    result_count = 0
    for signal_line in signal_array:
        signal_lookup = generate_signal_lookup(signal_line)
        result = lookup_result(signal_line, signal_lookup)
        result_list = list(str(result))
        matching_digits = [x for x in result_list if int(x) in [1, 4, 7, 8]]
        result_count += len(matching_digits)

    return result_count



def generate_signal_lookup(signal_line):
    signal_lookup = [None for x in range(10)]
    signal_line = signal_line[0]

    # Find the unique ones
    signal_lookup[1] = "".join(sorted([x for x in signal_line if len(x) == 2][0]))
    signal_lookup[4] = "".join(sorted([x for x in signal_line if len(x) == 4][0]))
    signal_lookup[7] = "".join(sorted([x for x in signal_line if len(x) == 3][0]))
    signal_lookup[8] = "".join(sorted([x for x in signal_line if len(x) == 7][0]))

    # Find the other ones
    signal_lookup[3] = "".join(sorted([x for x in signal_line if len(x) == 5 and set(signal_lookup[1]).issubset(set(x))][0]))
    signal_lookup[6] = "".join(sorted([x for x in signal_line if len(x) == 6 and not set(signal_lookup[1]).issubset(set(x))][0]))

    left_side_of_zero = set(signal_lookup[8]).symmetric_difference(signal_lookup[3])
    signal_lookup[0] = "".join(sorted([x for x in signal_line if len(x) == 6 and set(x) != set(signal_lookup[6]) and left_side_of_zero.issubset(set(x))][0]))
    signal_lookup[9] = "".join(sorted([x for x in signal_line if len(x) == 6 and set(x) != set(signal_lookup[6]) and set(x) != set(signal_lookup[0])][0]))

    bottom_part_of_one = list(set(signal_lookup[1]).intersection(signal_lookup[6]))[0]
    signal_lookup[5] = "".join(sorted([x for x in signal_line if len(x) == 5 and bottom_part_of_one in x and set(x) != set(signal_lookup[3])][0]))
    signal_lookup[2] = "".join(sorted([x for x in signal_line if len(x) == 5 and set(x) != set(signal_lookup[5]) and set(x) != set(signal_lookup[3])][0]))

    return signal_lookup


def lookup_result(signal_line, signal_lookup):
    result = ""
    sorted_signal_line = ["".join(sorted(x)) for x in signal_line[1]]
    for digit_idx in range(len(signal_line[1])):
        result += str(signal_lookup.index(sorted_signal_line[digit_idx]))
    return int(result)


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    seg_lines = []
    for line in lines:
        parts = line.strip().split("|")
        first_part = [x.strip() for x in parts[0].strip().split(" ")]
        second_part = [x.strip() for x in parts[1].strip().split(" ")]
        seg_lines.append((first_part, second_part))

    return seg_lines


if __name__ == "__main__":
    main()