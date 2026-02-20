from func import *

game_mode = int(input("Do you want a PvP or bot game? Answer with 1 for PvP or 0 for bot: "))
turn = input("Who play first X or O: ")

board = Board()

if game_mode == 1:
        if turn == 'X':
                first_player = Player(board, 'X')
                second_player = Player(board, 'O')
        else:
                first_player = Player(board, 'O')
                second_player = Player(board, 'X')
else:
        if turn == 'X':
                first_player = Bot(board, 'X')
                second_player = Player(board, 'O')
        else:
                first_player = Player(board, 'O')
                second_player = Bot(board, 'X')


while 1:
        if not board.empty_slots():
                print("It's a tie!!!")
                break
        first_player.play()
        winner = board.check_winner()
        if winner:
                print(f'Winner is the player with letter {winner}')
                break


        if not board.empty_slots():
                print("It's a tie!!!")
                break
        second_player.play()
        winner = board.check_winner()
        if winner:
                print(f'Winner is the player with letter {winner}')
                break

