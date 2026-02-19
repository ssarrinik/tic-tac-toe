from func import *

board = Board()
player1 = Player(board, 'X')
player2 = Player(board, 'O')

while not board.check_winner():
        player1.play()
        if board.check_winner():
                break
        player2.play()

