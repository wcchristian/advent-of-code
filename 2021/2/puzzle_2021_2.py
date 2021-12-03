import os

_filename = "input.txt"

def main():
    # Load in the file
    command_list = load_data()
    
    # Go through and find out how the things in the file affect the variables
    p1_position = p1_process_command_list(command_list)
    p2_position = p2_process_command_list(command_list)

    # Multiply and produce the output
    print(f"Part 1: The result of {p1_position} is {p1_position[0] * p1_position[1]}")
    print(f"Part 2: The result of {p2_position} is {p2_position[0] * p2_position[1]}")


"""Process the command list and determine the final position

:param command_list: The list of tuple "commands" to process
:return: tuple containing the final horizontal position and depth position (horizontal, depth)

"""
def p1_process_command_list(command_list):
    horizontal_position = 0
    depth = 0

    for command in command_list:
        command_direction = command[0]
        command_distance = command[1]


        match command_direction:
            case "forward":
                horizontal_position += command_distance
            case "backward":
                horizontal_position -= command_distance
            case "up":
                depth -= command_distance
            case "down":
                depth += command_distance

    return (horizontal_position, depth)


"""Process the command list considering aim up and down rather than depth

:param command_list: The list of tuple commands to process
:return: tuple containing the position and depth (horizontal, depth) 

"""
def p2_process_command_list(command_list):
    horizontal_position = 0
    aim = 0
    depth = 0

    for command in command_list:
        command_direction = command[0]
        command_distance = command[1]


        match command_direction:
            case "forward":
                horizontal_position += command_distance
                depth += command_distance * aim
            case "backward":
                horizontal_position -= command_distance
                depth -= command_distance * aim
            case "up":
                aim -= command_distance
            case "down":
                aim += command_distance

    return (horizontal_position, depth)


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