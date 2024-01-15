import numpy as np
import random



def final_greet():
    global play_or_not
    play_or_not = input('Do you want to play Tic Tac Toe again? [y/n]')
    if play_or_not == 'y':
        print("Okay, let's start another round")
    elif play_or_not == 'n':
        print('Thank you for playing, see you next time!')
    else:
        print('Invalid answer. Please try filling in "y" or "n".')
        final_greet()

def print_c_board():
    print(
        f"  {board[0, 0]}  |  {board[0, 1]}  |  {board[0, 2]}\n"
        f"-----------------\n"
        f"  {board[1, 0]}  |  {board[1, 1]}  |  {board[1, 2]}\n"
        f"-----------------\n"
        f"  {board[2, 0]}  |  {board[2, 1]}  |  {board[2, 2]}\n"
    )

def put_move(p):
    global game_over
    if p == 1:
        symbol = 'X'
    elif p==2:
        symbol = 'O'

    good_answer = False
    while good_answer == False:
        player_m = input(f'Player{p}: Where do you want to put your "{symbol}"?\n'
                          f'Note: Please give me the row and column number. Example: "1,2" means 1st row and 2nd column. '
                          f'(Do not put decimal numbers)\n')
        try:
            player_m_list = [int(n.strip()) - 1 for n in player_m.split(',')]
            if board[player_m_list[0], player_m_list[1]] == ' ':
                good_answer = True
                board[player_m_list[0], player_m_list[1]] = symbol
            else:
                print('This position has been taken. Please choose another one.')
        except:
            print('Your answer is not valid. Please try again.\n')


    print_c_board()

#### examine the winner
    c_board = (board == symbol).astype(int)
    row_sum = np.sum(c_board, axis=1)
    col_sum = np.sum(c_board, axis=0)
    main_diag_sum = np.diagonal(c_board).sum()
    flip_diag_sum= np.fliplr(c_board).diagonal().sum()
    total_fill = np.where((board == 'X')|(board == 'O'), 1, 0).sum()

    if (row_sum == 3).astype(int).sum() >= 1 or (col_sum == 3).astype(int).sum() >= 1 or main_diag_sum ==3  or flip_diag_sum ==3:
        print(f'Good Job player{p}! You have won the game.')
        game_over = True
    elif total_fill == 9:
        print('The board is filled up already. No one loses in this round :)')
        game_over = True
    else:
        game_over = False


play_or_not = input('Do you want to play Tic Tac Toe? [y/n]')
while play_or_not == 'y':
    print('''
    Welcome to Tic Tac Toe!
  _______ _____ _____   _______       _____   _______ ____  ______ 
 |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|
    | |    | || |         | |  /  \ | |         | | | |  | | |__   
    | |    | || |         | | / /\ \| |         | | | |  | |  __|  
    | |   _| || |____     | |/ ____ \ |____     | | | |__| | |____ 
    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|                                                    
    '''
    )
    board = np.array([
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ])
    print('Game start! Here is our board:')

    print_c_board()

    li = [1,2]
    first_p = random.choice([1,2])
    li.remove(first_p)
    second_p = li[0]

    print(f'Symbol:\nPlay1: X\nPlay2: O\n\nWe are doing a random draw to decide which player goes first......\n'
          f'Result: Play{first_p} can go first!\n\n')
    game_over = False

    while game_over == False:
        put_move(first_p)
        if game_over == True:
            break
        put_move(second_p)


    final_greet()







