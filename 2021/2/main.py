import os

_filename = "example_input.txt"

def main():
    # Load in the file
    command_list = load_data()

    # Initialize the variables

    # Go through and find out how the things in the file affect the variables
    position = process_command_list(command_list)

    # Multiply and produce the output
    print(f"The result of {position} is {position[0] * position[1]}")


"""Process the command list and determine the final position

:param command_list: The list of tuple "commands" to process
:return: tuple containing the final horizontal position and depth position (horizontal, depth)

"""
def process_command_list(command_list):
    for command in command_list:
        command_direction = command[0]
        command_distance = command[1]
        horizontal_position = 0
        depth = 0


        match command_direction:
            case "forward":
                horizontal_position += command_distance
            case "backward":
                horizontal_position -= command_distance
            case "up":
                depth -= command_distance
            case "down":
                depth += command_distance
            case _:
                break;

    return (2, 3)


"""Load the input file lines and set the command into a list of tuples.

:return: array of tuples containing direction and distance loaded from the file. (direction, distance)
"""
def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        content = f.readlines()

    command_list = []
    for line in content:
        split = line.split(" ")
        tup = (split[0], int(split[1]))
        command_list.append(tup)

    return command_list



if __name__ == "__main__":
    main()