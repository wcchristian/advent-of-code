import math
import os

_filename = "input.txt"

def main():
    print("\nDay 10: Syntax Scoring")
    print("==============================")
    syntax_lines = load_data()
    incomplete_chunks, corruption_score = find_broken_lines(syntax_lines)

    print(f"\np1: The corruption score is: {corruption_score}\n")

    autocomplete_scores = complete_incomplete_lines(incomplete_chunks)
    middle_score = find_middle_score(autocomplete_scores)

    print(f"p2: The middle autocomplete score is: {middle_score}\n")


def find_middle_score(scores):
    scores = sorted(scores)
    middle_index = math.ceil(len(scores) / 2) - 1
    return scores[middle_index]


def complete_incomplete_lines(incomplete_chunks):
    autocomplete_scores = []
    for line in incomplete_chunks:
        autocomplete_score = 0
        chars_added = []
        reversed_line = line[::-1]
        for char in list(reversed_line):
            chars_added.append(invert_char(char))
        
        for added_char in chars_added:
            autocomplete_score = autocomplete_score * 5 + find_autocomplete_score(added_char)

        autocomplete_scores.append(autocomplete_score)

    return autocomplete_scores



def find_broken_lines(syntax_lines):
    corrupted_lines = []
    incomplete_chunks = []
    corruption_score = 0
    for line in syntax_lines:
        line_chunks = []
        
        for char_idx in range(len(line)):
            if line[char_idx] in ['(', '[', '<', '{']:
                line_chunks.append(line[char_idx])
            elif line[char_idx] in [')', ']', '>', '}'] and invert_char(line[char_idx]) == line_chunks[-1]:
                idx_of_opening = find_index_of_opening(line[char_idx], line_chunks)
                del line_chunks[idx_of_opening:char_idx+1]
            else:
                corrupted_lines.append(line)
                corruption_score += find_corrupted_score(line[char_idx])
                line_chunks = []
                break
        
        if len(line_chunks) > 0:
            incomplete_chunks.append("".join(line_chunks))

    return (incomplete_chunks, corruption_score)


def find_index_of_opening(char, line_chunks):
    reverse_line = line_chunks[::-1]
    for char_idx in range(len(reverse_line)):
        if reverse_line[char_idx] == invert_char(char):
            return len(reverse_line) - char_idx - 1


def find_corrupted_score(char):
    match char:
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137


def find_autocomplete_score(char):
    match char:
        case ')': return 1
        case ']': return 2
        case '}': return 3
        case '>': return 4


def invert_char(char):
    match char:
        case '(': return ')'
        case ')': return '('
        case '[': return ']'
        case ']': return '['
        case '{': return '}'
        case '}': return '{'
        case '<': return '>'
        case '>': return '<'


def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        lines = f.readlines()

    return [x.strip() for x in lines]


if __name__ == "__main__":
    main()