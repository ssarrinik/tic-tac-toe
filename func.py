import time

MATRIX_SIZE = 4

class Player:

    def __init__(self, board, char):
        self.character = char
        self.board = board

    def ask_move(self):
        ask_again = 1
        x = y = 0

        while ask_again:
            try:
                x, y = input("Enter position you want to play in format x,y: ").split(',')
                x = int(x)
                y = int(y)
            except NameError:
                print("Oups... x,y must be integer values with ',' in between!")
            except ValueError:
                print("Oups... x,y must be integer values with ',' in between!")
            else:
                if not self.board.check_if_slot_empty(x, y):
                    print("The slot is already filled!")
                    ask_again = 1
                else:
                    ask_again = 0
        return x, y

    def play(self):
        x = 0
        y = 0

        x, y = self.ask_move()
        if self.board.check_if_slot_empty(x, y):
            self.board.put_player(x, y, self.character)

        self.board.print_board()


def check_winner_by_rows(matrix):
    ones = 0
    two = 0
    for row in matrix:
        for num in row:

            if num == 'X':
                ones += 1
            elif num == 'O':
                two += 1

        # print(f"The number of X is {ones} in row {row}")
        # print(f"The number of O is {two} in row {row}\n")

        if ones == MATRIX_SIZE:
            return 'X'
        elif two == MATRIX_SIZE:
            return 'O'

        ones = 0
        two = 0

    return check_diagonals(matrix)


def check_diagonals(matrix):
    n = len(matrix)

    main_diag = [matrix[i][i] for i in range(n)]
    if all(cell == main_diag[0] and cell != ' ' for cell in main_diag):
        return main_diag[0]

    anti_diag = [matrix[i][n - 1 - i] for i in range(n)]
    if all(cell == anti_diag[0] and cell != ' ' for cell in anti_diag):
        return anti_diag[0]

    return ' '


class Board:

    def __init__(self):
        self.arr = [[ ' ' for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    def check_if_slot_empty(self, x, y):
        if self.arr[y][x] != ' ':
            return False

        return True

    def put_player(self, x, y, char):
        self.arr[y][x] = char

    def check_winner(self):

        winner = check_winner_by_rows(self.arr)
        if winner == 'X' or winner == 'O':
            return winner
        transpose_matrix = list(zip(*self.arr))

        winner = check_winner_by_rows(transpose_matrix)
        if winner == 'X' or winner == 'O':
            return winner

    def print_board(self):

        for j in range(MATRIX_SIZE-1, -1, -1):
            row = self.arr[j]
            print('   ', end='')
            for i, num in enumerate(row):
                if i < MATRIX_SIZE-1:
                    print(f"{num}|", end='')
                else:
                    print(num)
            if j > 0:
                print('   ' + '------')

    def empty_slots(self):
        for row in self.arr:
            for n in row:
                if n == ' ':
                    return True
        return False

    def remove_slot(self, x, y):
        self.arr[y][x] = ' '

    def get_available_moves(self):
        moves = []
        for i, row in enumerate(self.arr):
            for j, num in enumerate(row):
                if num == ' ':
                    moves.append((j, i))

        return moves


class Bot(Player):

    def __init__(self, board, char):
        super().__init__(board, char)

    def play(self):
        depth = 0
        best_x = 0
        best_y = 0
        best_score = -float('inf')

        start_time = time.time()
        for move in self.board.get_available_moves():
            print(f"We started evaluating the next slot.")
            x, y = move
            self.board.put_player(x, y, self.character)

            # score = self.maxing(depth + 1, False)
            score = self.alfabeta(depth+1, -float('inf'), float('inf'), False)
            self.board.remove_slot(x, y)

            if best_score < score:
                best_score = score
                best_x = x
                best_y = y
        print(f'Time of executions is sec {time.time() - start_time}')

        if self.board.check_if_slot_empty(best_x, best_y):
            self.board.put_player(best_x, best_y, self.character)
        else:
            print('Slot is already filled.')

        self.board.print_board()

    def maxing(self, depth, is_maxing):
        if self.character == 'X':
            char = 'O'
        else:
            char = 'X'

        winner = self.board.check_winner()
        if winner == self.character:
            return 10
        if winner == char:
            return -10
        if not self.board.empty_slots():
            return 0
        # if depth == 6:
        #     return 0

        if is_maxing:
            best_score = -float('inf')
            for move in self.board.get_available_moves():
                x, y = move
                self.board.put_player(x, y, self.character)
                score = self.maxing(depth + 1, False)
                self.board.remove_slot(x, y)
                if score > best_score:
                    best_score = score
            return best_score
        else:
            best_score = float('inf')
            for move in self.board.get_available_moves():
                x, y = move
                if self.character == 'X':
                    char = 'O'
                else:
                    char = 'X'
                self.board.put_player(x, y, char)
                score = self.maxing(depth + 1, True)
                self.board.remove_slot(x, y)
                if score < best_score:
                    best_score = score
            return best_score

    def alfabeta(self, depth, a, b, is_maxing):
        winner = self.board.check_winner()
        if self.character == 'X':
            char = 'O'
        else:
            char = 'X'

        if winner == self.character:
            return 10
        if winner == char:
            return -10
        if not self.board.empty_slots():
            return 0

        if is_maxing:
            value = -float('inf')
            for move in self.board.get_available_moves():
                x, y = move
                self.board.put_player(x, y, self.character)
                value = max(value, self.alfabeta(depth + 1, a, b, False))
                self.board.remove_slot(x, y)
                if value >= b:
                    break
                a = max(a, value)
            return value
        else:
            value = float('inf')
            for move in self.board.get_available_moves():
                x, y = move
                self.board.put_player(x, y, char)
                value = min(value, self.alfabeta(depth + 1, a, b, True))
                self.board.remove_slot(x, y)
                if value <= a:
                    break
                b = min(b, value)
            return value


