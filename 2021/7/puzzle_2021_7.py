import os

_filename = "input.txt"

def main():
    print("Day 7: The Treachery of Whales")
    print("==============================\n")

    crab_array = load_data()
    fuel_position_array = find_fuel_for_positions(crab_array)
    smallest_fuel_location_and_position = find_least_fuel_and_position(fuel_position_array)
    smallest_fuel_amount = smallest_fuel_location_and_position[0]
    smallest_fuel_location = smallest_fuel_location_and_position[1]

    print(f"\n\nThe best position is: {smallest_fuel_location} with fuel cost: {int(smallest_fuel_amount)}")


def find_max_position(crab_array):
    return max(crab_array)


def find_fuel_for_positions(crab_array):
    fuel_position_array = [0 for i in range(max(crab_array) + 1)]
    for goal_position in range(max(crab_array) + 1):
        print(f"Testing Position: {goal_position}/{max(crab_array)+1}", end="\r")
        total_fuel_used = 0
        for crab_position in crab_array:
            # find out how far movement is
            spaces_moved = abs(goal_position - crab_position)
            fuel_used = ((spaces_moved ** 2 + spaces_moved) / 2)
            total_fuel_used += fuel_used

        fuel_position_array[goal_position] = total_fuel_used

    return fuel_position_array

def find_least_fuel_and_position(fuel_position_array):
    smallest_fuel_cost = min(fuel_position_array)
    smallest_fuel_location = fuel_position_array.index(smallest_fuel_cost)
    return (smallest_fuel_cost, smallest_fuel_location)



def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        line = f.readline()

    return [int(x) for x in line.strip().split(",")]


if __name__ == "__main__":
    main()