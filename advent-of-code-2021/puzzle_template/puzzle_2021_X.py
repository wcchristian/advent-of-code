import os

_filename = "example_input.txt"

def main():
    print("\nDay 7: The Treachery of Whales")
    print("==============================")

    print(f"\nThe answer is {1}")

def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    return lines


if __name__ == "__main__":
    main()