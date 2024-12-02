import os

def main():
    filename = "day2_input.txt"
    example_filename = "day2_example.txt"

    print(f'Part 1 Example: {part1(example_filename)}')
    print(f'Part 1: {part1(filename)}')
    print(f'Part 2 Example: {part2(example_filename)}')
    print(f'Part 2: {part2(filename)}')
    

def part1(filename):
    reports = read_input(filename)
    count = 0

    for report in reports:
        if is_report_safe(report):
            count += 1

    return count


def part2(filename):
    reports = read_input(filename)
    count = 0

    for report in reports:
        if is_report_safe(report):
            count += 1
            continue

        for i in range(len(report)):
            report_copy = report.copy()
            del report_copy[i]
            if is_report_safe(report_copy):
                count += 1
                break

    return count

def is_report_safe(report):
    good_report = True

    difference = abs(report[0] - report[1])
    if difference < 1 or difference > 3:
        return False

    increasing = report[0] < report[1]

    for i in range(1, len(report) - 1):

        difference = abs(report[i] - report[i+1])
        if(difference < 1 or difference > 3):
            good_report = False
            break


        if increasing and report[i] >= report[i+1]:
            good_report = False
            break

        if not increasing and report[i] <= report[i+1]:
            good_report = False
            break

    return good_report

def read_input(filename):
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, filename)
    file = open(filepath, 'r')
    file_lines = file.readlines()

    reports = [[int(num) for num in x.split(" ")] for x in file_lines]
    return reports


if __name__ == "__main__":
    main()