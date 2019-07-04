'''Tic Tac Toe Game
2 players are sitting in front of the same computer and playing the game Tic Tac Toe.
Player1 is given the option to choose the symbol X or O.
If Player1 chooses X, he goes first or else Player2 goes first.
The empty game board is outputted.
Game Board is of the layout of the number keypad in a keyboard.
Player is asked for the position he wants to mark from [1-9].
The game board will be updated with that player's mark in that position.
The game continues till a winner is found. 
Once a winner is found, the winner will be declared and the user will be given the option to
play the game again or to quit.
'''

def update_board(d):
    print(f" {d['7']} | {d['8']} | {d['9']} \n---+---+---\n {d['4']} | {d['5']} | {d['6']} \n---+---+---\n {d['1']} | {d['2']} | {d['3']} \n")

def get_position(sym, d):
    pos = input("Choose your next position: (1-9)\n")
    if d[pos] != ' ':
        print('Wrong position! Position already filled!')
        wrong_pos = True
    else:
        d[pos] = sym
        wrong_pos = False
    return d,wrong_pos

def win_patterns(d,sym_x,sym):
    for index,value in enumerate(d.values()):
        if value == ' ':
            if d['7'] == d['8'] == d['9'] != ' ' or d['4'] == d['5'] == d['6'] != ' ' or d['1'] == d['2'] == d['3'] != ' ' or d['7'] == d['4'] == d['1'] != ' ' or d['8'] == d['5'] == d['2'] != ' ' or d['9'] == d['6'] == d['3'] != ' ' or d['7'] == d['5'] == d['3'] != ' ' or d['9'] == d['5'] == d['1'] != ' ':
                who_won(sym_x,sym)
                return True
                break
            else:
                return False
    else:
        print('GAME OVER!')
        return True

def which_symbol(s,wrong_pos):
    if wrong_pos == True:
        if s == 'X':
            s = 'X'
        else:
            s = 'O'
    else:
        if s == 'X':
            s = 'O'
        else:
            s = 'X'
    return s

def who_won(sym_x,sym):
    if sym.upper() == 'X':
        if sym_x == 'Player 1':
            winner = 'Player 1'
        else:
            winner = 'Player 2'
    elif sym.upper() == 'O':
        if sym_x == 'Player 1':
            winner = 'Player 2'
        else:
            winner = 'Player 1'
    print(f"\nCongratulations! {winner} has won the game \n")


print('Welcome to Tic Tac Toe Game \n')

while True:

    game_board = {'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ','2':' ','3':' '}

    symbol = input('Player 1: Do you want to be X or O? \n')
    if symbol.upper() == 'X':
        print('Player 1 will go first. \n')
        sym_X = 'Player 1'
    else:
        print('Player 2 will go first. \n')
        sym_X = 'Player 2'


    start_game = input('Are you ready to play? Y/N \n')
    #depending on Y/N, the game will start or not start.
    
    #If Y, the game starts aka the while loop starts

    if start_game.upper() == 'Y':
        update_board(game_board)
        symbol = 'X'
        while True:
            game_board, wrong_pos = get_position(symbol,game_board)
            #update game board
            update_board(game_board)

            #check for a winner - Y - declare winner; N - continue the loop
            #declare winner
            winner_status = win_patterns(game_board,sym_X,symbol)
            if winner_status == True:
                break
            else:
                symbol = which_symbol(symbol,wrong_pos)
                continue
            #END INNER WHILE LOOP

    start_game = input('Do you want to play again? Y/N  \n')

    #Depending on the user input, it goes out of the while loop or stays in the while loop.
    if start_game.upper() == 'Y':
        continue
    else:
        break

