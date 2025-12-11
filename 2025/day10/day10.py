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
    _, buttons, joltages = parse_line(line)

    opt = Optimize()
    presses = [Int(f"press_{idx}") for idx in range(len(buttons))]

    for press in presses:
        opt.add(press >= 0)

    for counter_idx, joltage in enumerate(joltages):
        contributions = [presses[idx] for idx, button in enumerate(buttons) if counter_idx in button]
        expression = Sum(contributions) if contributions else 0
        opt.add(expression == joltage)

    opt.minimize(Sum(presses))
    if opt.check() != sat:
        return None

    model = opt.model()
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