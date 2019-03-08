import random
def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_input():
    marker = ''
    #WHILE LOOP for asking for the correct output
    while marker != 'X' and marker != 'O':
        marker = input('Welcome sir or madam, please enter a valid option for your marker: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[7] == board[8] == board[9] == mark) or 
            (board[7] == board[4] == board[1] == mark) or 
            (board[5] == board[8] == board[2] == mark) or 
            (board[6] == board[3] == board[9] == mark) or 
            (board[7] == board[5] == board[3] == mark) or 
            (board[1] == board[5] == board[9] == mark))
def choose_first():
    if random.randint(0, 1) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for num in range(1,10):
        if space_check(board, num):
            return False
    return True
def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Please choose a position on da board(1-9): '))
    
    return position
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
#The Game
print('Welcome to Tic Tac Toe!')

#Next Gen Gameplay Mechanics
while True:
    # -----Setup------
    the_board = [' ']*10
    input_1, input_2 = player_input()
    turn = choose_first()
    print(f'{turn} will go first')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game = True
    else:
        game = False
    # ----Gameplay----
    while game:
        if turn == 'Player 1':
            # Show board
            display_board(the_board)
            # Pick position
            position = player_choice(the_board)
            # Place Marker
            place_marker(the_board, input_1, position)
            # Win Check
            if win_check(the_board, input_1):
                display_board(the_board)
                print('Player 1 has demolished Player 2')
                game = False
            # Tie Check
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Draw!')
                    game = False
            # Switch turns
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, input_2, position)
            if win_check(the_board, input_2):
                display_board(the_board)
                print('Player 2 has demolished Player 1')
                game = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Draw!')
                    game = False
                else:				
                    turn = 'Player 1'
        #REPLAY
    if not replay():
        break
            
