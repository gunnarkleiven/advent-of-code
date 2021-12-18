class Board:
    def __init__(self):
        self.board = []
        self.prev_called = 0

    def add_row(self, row):
        self.board.append(row)

    def mark_number(self, number):
        self.prev_called = number
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == number:
                    # Handle the 0 value
                    if self.board[y][x] == 0:
                        self.board[y][x] = float('-inf')
                    else:
                        self.board[y][x] = -self.board[y][x]
                    return

    def has_won(self):
        # Check all columns
        for x in range(5):
            if all([self.board[y][x] < 0 for y in range(5)]):
                # print(f'winning column: {x}')
                return True
        # Check all rows
        for y in range(5):
            if all([self.board[y][x] < 0 for x in range(5)]):
                # print(f'winning row: {y}')
                return True
        return False

    def calculate_result(self):
        unmarked = []
        for y in range(5):
            for x in range(5):
                if self.board[y][x] > -1:
                    unmarked.append(self.board[y][x])
        res = sum(unmarked) * self.prev_called
        return res

    def __str__(self):
        str_version = ""
        for x in self.board:
            str_version += " ".join(str(y) for y in x)
            str_version += "\n"
        return str_version


def create_boards(data):
    boards = []
    pointer = 1
    while pointer < len(data):
        if data[pointer] == "":
            pointer += 1
            board = Board()
            for x in range(5):
                row = [int(x) for x in data[pointer + x].split()]
                # print(f'Row: {row}')
                board.add_row(row)
            # print(f'Board:\n{board}')
            boards.append(board)
            pointer += 5

    return boards


def add_numbers_to_board(numbers, boards):
    for n in numbers:
        for board in boards:
            board.mark_number(n)
            if board.has_won():
                print(f'Board won!\n{board}')
                return board.calculate_result()

    return -1


def solve_part1(data):
    # numbers = [int(x) for x in data[0].split(',')]
    numbers = [int(x) for x in data[0].split(",")]
    # print(f'numbers = {numbers}')

    boards = create_boards(data)

    result = add_numbers_to_board(numbers, boards)
    if result != -1:
        print(f'Result: {result}')
    else:
        print(f'Error! No winning board')


def add_numbers_to_board_get_last_win(numbers, boards):
    wins = [False for _ in range(len(boards))]
    last_win_index = -1
    for n in numbers:
        for i in range(len(boards)):
            # If it has already won, skip it
            if wins[i]:
                continue
            boards[i].mark_number(n)
            if boards[i].has_won():
                wins[i] = True
                last_win_index = i
    print(f'Last board to win is id {last_win_index}')
    res = boards[last_win_index].calculate_result()
    return res


def solve_part2(data):
    # numbers = [int(x) for x in data[0].split(',')]
    numbers = [int(x) for x in data[0].split(",")]
    # print(f'numbers = {numbers}')

    boards = create_boards(data)

    result = add_numbers_to_board_get_last_win(numbers, boards)
    print(f'Result = {result}')

if __name__ == '__main__':
    with open('day4.txt', 'r') as reader:
        data = [x.strip() for x in reader.readlines()]
    # solve_part1(data)
    # solve_part1(data)
    solve_part2(data)
