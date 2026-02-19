class Player:

    def __init__(self, board, char):
        self.character = char
        self.board = board

    def play(self):
        x = 0
        y = 0
        ask_again = 1
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
                ask_again = 0

        if self.board.check_if_slot_empty(x, y):
            self.board.put_player(x, y, self.character)
        else:
            print("The slot is already filled!")

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

        if ones == 3:
            print("The player1 is the winner")
            return 1
        elif two == 3:
            print("The player2 is the winner")
            return 2

        ones = 0
        two = 0

    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ':
        print(f"The player{not(matrix[0][0] == 'X')} is the winner")
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[1][1] != ' ':
        print(f"The player{matrix[1][1] == 'O'} is the winner")
        return matrix[0][2]

    return 0


class Board:

    def __init__(self):
        self.arr = [[ ' ' for _ in range (3)] for _ in range(3)]

    def check_if_slot_empty(self, x, y):
        if self.arr[x][y] != ' ':
            return False

        return True

    def put_player(self, x, y, char):
        self.arr[x][y] = char

    def check_winner(self):

        if check_winner_by_rows(self.arr):
            return True

        transpose_matrix = list(zip(*self.arr))

        if check_winner_by_rows(transpose_matrix):
            return True

    def print_board(self):

        for j in range(2, -1, -1):
            row = self.arr[j]
            print('   ', end='')
            for i, num in enumerate(row):
                if i < 2:
                    print(f"{num}|", end='')
                else:
                    print(num)
            if j > 0:
                print('   ' + '------')
