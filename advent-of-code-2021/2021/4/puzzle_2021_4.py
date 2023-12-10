import os

# Config
_filename = "input.txt"
_last_winning_board = []
_calls_when_last_board_won = []

def main():
    data = load_data()
    calls = data[0]
    boards = data[1]

    winning_and_calls = find_first_winning_board(calls, boards)
    winning_board = winning_and_calls[0]
    calls_so_far = winning_and_calls[1]

    result_part_one = calculate_result(winning_board, calls_so_far)

    winners_and_calls = find_last_winning_board_result(calls, boards)
    result_part_two = calculate_result(winners_and_calls[0][-1], winners_and_calls[1])

    print(f"\nThe result for part one is {result_part_one}")

    print(f"\n===================================")

    print(f"\nThe result for part two is {result_part_two}")


def calculate_result(board, calls_so_far):
    numbers = []
    for line in board:
        for char in line:
            if char not in calls_so_far:
                numbers.append(int(char))

    return sum(numbers) * int(calls_so_far[-1])

def find_last_winning_board_result(calls, boards):
    calls_so_far = []
    winner_list = []
    boards_left = boards.copy()
    for call in calls:
        if len(boards_left) == 0:
            return (winner_list, calls_so_far)
        calls_so_far.append(call)

        winning_boards = check_for_winners(calls_so_far, boards_left)
        
        for board in winning_boards:
            boards_left.remove(board)
            winner_list.append(board)


def find_first_winning_board(calls, boards):
    calls_so_far = []
    for call in calls:
        calls_so_far.append(call)
        winning_boards = check_for_winners(calls_so_far, boards)
        if len(winning_boards) == 1:
            break;
    return (winning_boards[0], calls_so_far);


def check_for_winners(calls, boards):
    winning_boards = []
    for board_idx in range(len(boards)):
        is_winner = check_board_for_win(calls, boards[board_idx])
        if is_winner:
            winning_boards.append(boards[board_idx])
    return winning_boards 


def check_board_for_win(calls, board):
    is_horizontal_win = False
    is_vertical_win = False

    for horizontal_line in board:
        is_horizontal_win = check_line_for_win(calls, horizontal_line)
        if is_horizontal_win:
            break

    column_count = len(board[0])
    for col in range(column_count):
        # for each line, grab the char in this col and add to an array
        vertical_line = []
        for h_line in board:
            vertical_line.append(h_line[col])
        is_vertical_win = check_line_for_win(calls, vertical_line)

    if is_horizontal_win or is_vertical_win:
        global _last_winning_board
        global _calls_when_last_board_won
        _last_winning_board = board
        _calls_when_last_board_won = calls

    return is_horizontal_win or is_vertical_win


def check_line_for_win(calls, line):
    is_win = True
    for num in line:
        if num not in calls:
            is_win = False
            break
    return is_win

def print_board(board, calls):
    for line in board:
        for char in line:
            if calls != None and char in calls:
                print("x ", end='')
            else:
                print(f"{char} ", end='')
        print()

def load_data():
    script_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_path, _filename)

    with open(filepath) as f:
        called_numbers = f.readline().strip()
        lines = f.readlines()

    boards = []
    board_lines = []
    for line in lines:
        if line == "end" or (line == "\n" and len(board_lines) > 0):
            boards.append(board_lines)
            board_lines = []
        elif line != "\n":
            split_line = line.strip().split(" ")
            split_line = [x.strip() for x in split_line if x != ""]
            board_lines.append(split_line)

    called_numbers_array = called_numbers.split(",")
    return (called_numbers_array, boards)


if __name__ == "__main__":
    main()