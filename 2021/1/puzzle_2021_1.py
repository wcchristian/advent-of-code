import os

# Config Area
_filename = "input.txt"

def main():
    # Load an array of numbers from the file
    single_depth_array = load_num_array()

    # Process into the list of sliding window sums
    window_depth_array = process_window_array(single_depth_array)

    # Process numbers and keep track of how many increase
    p1_deeper_count = count_depth_increase(single_depth_array)
    p2_deeper_count = count_depth_increase(window_depth_array)

    # Log the result
    print(f"Puzzle 1: There were {p1_deeper_count} times that it got deeper")
    print(f"Puzzle 2: There were {p2_deeper_count} times that it got deeper")

"""Processes the single value array and splits it up into windows of 3
   it loops from the 2nd element to the 2nd to last (since they cant make a list of three)
   and sums the previous, current, and next items.

   :param depth_array: The single value array to be processed
   :returns: array of the sums
"""
def process_window_array(depth_array):
    window_sums = []
    for idx in range(1, len(depth_array) - 1):
        sum = depth_array[idx-1] + depth_array[idx] + depth_array[idx+1]
        window_sums.append(sum)

    return window_sums

"""Go through an array of ints and count each time the current value is larger than the previous value
   Skips first number in the array since it cant be larger or smaller since nothing is before it.

   :param depth_array: the array to iterate over
   :return: the int number of times that the value was greater than the one that came before it.
"""
def count_depth_increase(depth_array):
    prev_depth = depth_array[0];
    deeper_count = 0;

    for depth in depth_array[1:]:
        if(prev_depth < depth): 
            deeper_count += 1

        prev_depth = depth
    return deeper_count


"""Load the input file lines and convert them into integers.

   :return: array of integers loaded from the file.
"""
def load_num_array():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        content = f.readlines()

    return [int(x) for x in content]


if __name__ == "__main__":
    main()