import os
import time

# config
_filename = "input.txt"
_number_of_days = 256
_show_processing = True


def main():
    print("Day 6: Lanternfish")
    print("=========================\n")

    starting_fish_array = load_data()
    fish_count_array = init_fish_count_array(starting_fish_array)
    fish_count_array = process_days(fish_count_array, _number_of_days)
    total_fish_count = sum_fish_count(fish_count_array)

    print(f"The number of fish after {_number_of_days} days is {total_fish_count}")


def process_days(fish_count_array, num_days):
    fish_count_ary = fish_count_array.copy()
    for day in range(num_days):
        show_processing(fish_count_ary, day, num_days)

        num_new_fish = fish_count_ary[0]

        for fish_count_idx in range(1, 9):
            fish_to_move = fish_count_ary[fish_count_idx]
            fish_count_ary[fish_count_idx-1] = fish_to_move
            fish_count_ary[fish_count_idx] = 0

        fish_count_ary[6] += num_new_fish
        fish_count_ary[8] += num_new_fish
    return fish_count_ary
    

def show_processing(fish_count_array, day, num_days):
    if _show_processing:
        time.sleep(0.05)
        print(f"Day: {day+1}/{num_days} /// {fish_count_array}", end="\r")
        if day+1 == num_days:
            print()

def init_fish_count_array(fish_array):
    fish_count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in fish_array:
        fish_count_array[fish] += 1

    return fish_count_array


def sum_fish_count(fish_count_array):
    total_fish = 0
    for fish_count in fish_count_array:
        total_fish += fish_count
    return total_fish


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        line = f.readline()

    return [int(x) for x in line.strip().split(",")]

if __name__ == "__main__":
    main()