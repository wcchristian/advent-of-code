from collections import deque
from pathlib import Path
import re
from z3 import Int, Optimize, Sum, sat

def main():
    filename = "day10_input.txt"
    example_filename = "day10_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')

# Used BFS for this one.
def part1(filename):
    lines = read_file(filename)
    return sum(find_min_button_presses(line) for line in lines)


# Gave up on this one and looked up some solutions on reddit.
# found a hint to use a solver like z3 so gave that a shot.
# Most of the code in the below find_min_button_presses_for_joltages function
# is ai generated, with comments. Spent some time after generation learning
# how this worked. Definitely a tool I will have to use in future years.
# TODO: I should revisit this and try and use linear equations and Gaussian elimination to try and solve without
# the library. Gaussian Elimination.
def part2(filename):
    lines = read_file(filename)
    return sum([find_min_button_presses_for_joltages(line) for line in lines])


def find_min_button_presses(line):
    solution, buttons, _ = parse_line(line)
    start_state = '.' * len(solution)

    if start_state == solution:
        return 0

    queue = deque([(start_state, 0)])
    visited = {start_state}

    while queue:
        state, presses = queue.popleft()

        for button in buttons:
            new_state = list(state)
            for index in button:
                new_state[index] = '#' if new_state[index] == '.' else '.'
            new_state = ''.join(new_state)

            if new_state == solution:
                return presses + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return None


def find_min_button_presses_for_joltages(line):
    # Parse this machine's configuration into buttons and target joltages.
    _, buttons, joltages = parse_line(line)

    # Create an optimization context that can both constrain and minimize.
    opt = Optimize()
    # One integer decision variable per button counting how many times it is pressed.
    presses = [Int(f"press_{idx}") for idx in range(len(buttons))]

    # Constrain every button press count to be non-negative.
    for press in presses:
        opt.add(press >= 0)

    # Constrain each counter so its button contributions add up to the target joltage.
    for counter_idx, joltage in enumerate(joltages):
        # Collect the press variables for buttons wired to this counter.
        contributions = [presses[idx] for idx, button in enumerate(buttons) if counter_idx in button]
        # Sum those contributions, or treat it as zero if no button touches the counter.
        expression = Sum(contributions) if contributions else 0
        # Force the summed presses to match the required joltage for this counter.
        opt.add(expression == joltage)

    # Ask Z3 to minimize the total number of button presses across all variables.
    opt.minimize(Sum(presses))

    # Extract the optimal solution that meets every constraint.
    model = opt.model()
    # Add up each button's press count from the model so we can return the total cost.
    return sum(model[press].as_long() for press in presses)


def parse_line(line):
    # Extract the Solution
    solution = re.search(r'\[(.*)\]', line).group(1)

    # Extract the Buttons
    button_splits = re.findall(r'\(.*\)', line)[0].split(' ')
    buttons = []
    for button in button_splits:
        buttons.append(list(map(int, button.strip('()').split(','))))

    # Extract the Joltages
    joltages = re.findall(r'\{.*\}', line)
    joltages = [int(x) for x in joltages[0].strip('{}').split(',')]

    return solution, buttons, joltages


# Read the file in this directory given a file name
def read_file(filename):
    path = Path(__file__).parent / filename
    with open(path, 'r') as f:
        data = f.read().strip().splitlines()
    return data


if __name__ == "__main__":
    main()