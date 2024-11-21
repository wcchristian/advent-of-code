import os

_filename = "input.txt"

def main():
    print(f"Input File: {_filename}\n")

    line_array = load_data()
    result_tuple = find_gamma_epsilon(line_array)
    result_number = result_tuple[0] * result_tuple[1]

    print("Part 1:")
    print(f"Gamma is {result_tuple[0]}, Epsilon is {result_tuple[1]}")
    print(f"Result Number is: {result_number}\n")

    oxygen = filter_msb(line_array, 0, 1)
    co2 = filter_msb(line_array, 1, 0)
    result_number_2 = oxygen * co2

    print("Part 2:")
    print(f"Oxygen is {oxygen}, co2 is {co2}")
    print(f"Result Number is: {result_number_2}")


def find_gamma_epsilon(line_array):
    total_lines = len(line_array)
    num_digits = len(list(line_array[0]))
    
    num_occurrances = [0] * num_digits
    for line in line_array:
        digits = list(line)
        for idx in range(num_digits):
            num_occurrances[idx] += int(digits[idx])

    gamma_rate = ["0"] * num_digits
    epsilon_rate = ["0"] * num_digits
    for idx in range(num_digits):
        if(num_occurrances[idx] >= total_lines / 2):
            gamma_rate[idx] = "1"
        else:
            epsilon_rate[idx] = "1"


    gamma_rate_int = bin_string_to_int("".join(gamma_rate))
    epsilon_rate_int = bin_string_to_int("".join(epsilon_rate))

    return (gamma_rate_int, epsilon_rate_int)

def filter_msb(line_array, num_to_remove_if_msb_is_one, num_to_remove_if_msb_is_zero):
    filtered_array = line_array.copy()
    num_digits = len(list(filtered_array[0]))

    for digit_index in range(num_digits):

        if len(filtered_array) <= 1:
            break;

        one_count = 0
        for line in filtered_array:
            line_digs = list(line)
            one_count += int(line_digs[digit_index])


        # If one is msb, collect all lines that have 0 and remove them
        lines_to_remove = []
        if one_count >= len(filtered_array) / 2:
            # MSB is one, remove all lines at this digit that are 0
            for line in filtered_array:
                line_digs = list(line)
                if(int(line_digs[digit_index]) == num_to_remove_if_msb_is_one):
                    lines_to_remove.append(line)
        else:
            # MSB is zero, remove all lines at this digit that are 1
            for line in filtered_array:
                line_digs = list(line)
                if(int(line_digs[digit_index]) == num_to_remove_if_msb_is_zero):
                    lines_to_remove.append(line)


        for line in lines_to_remove:
            filtered_array.remove(line)

    return bin_string_to_int(filtered_array[0])


def bin_string_to_int(bin_string):
    bin_string = "0b" + bin_string
    return int(bin_string, base=2)


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    return [x.strip() for x in lines]


if __name__ == "__main__":
    main()