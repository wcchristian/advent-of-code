import os

_filename = "input.txt"

def main():
    print("\nDay 1: Report Repair")
    print("==============================")
    report = load_data()
    product_of_2020_numbers = product_of_2020_sum(report)

    print(f"\nThe answer is {product_of_2020_numbers}")


def product_of_2020_sum(report):
    for line in report:
        for line2 in report:
            for line3 in report:
                if int(line.strip()) + int(line2.strip()) + int(line3.strip()) == 2020:
                    return (int(line.strip()) * int(line2.strip()) * int(line3.strip()))


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    return lines


if __name__ == "__main__":
    main()