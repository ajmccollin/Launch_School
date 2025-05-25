import random
import os
import time

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_NUMBER = 3

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7],            # diagonals
    ]

def prompt(message):
    print(f'==> {message}')

def join_or(num_range, delimiter=', ', connector='or'):
    match len(num_range):
        case 0:
            return ''
        case 1:
            return str(num_range)
        case 2:
            return f"{num_range[0]} {connector} {num_range[1]}"
    
    starting_nums = delimiter.join(str(num) for num in num_range[0: -1])
    return f'{starting_nums} {connector} {num_range[-1]}'

def display_board(board):
    os.system('clear')

    prompt(f"You are {PLAYER_MARKER}. The Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def display_round(standings):
        print(f"********* ROUND {standings['Round Number']} *********")

def display_score(standings):
        prompt(f"The current score is: "
                f"[{standings['Player Score']}:"
                f"{standings['Computer Score']}]")

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid square.")

    board[int(square)] = PLAYER_MARKER

# def find_at_risk_square(board, line): #FIX
#     if lines.count(PLAYER_MARKER) == 2:
#         for square in lines:
#             if board[square] == INITIAL_MARKER:
#                 return board[square]
    
def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    #if find_at_risk_square(board) == True:
    #    print(find_at_risk_square(board))
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER


def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER 
                and board[sq2] == PLAYER_MARKER 
                and board[sq3] == PLAYER_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def reset_scores(standings):
    standings['Player Score'] = 0
    standings['Computer Score'] = 0
    standings['Round Number'] = 1

def play_tic_tac_toe():
    current_standings = {
        'Player Score': 0,
        'Computer Score': 0,
        'Round Number': 1,
    }
        
    while True:
        board = initialize_board()

        while True:
            display_board(board)
            display_round(current_standings)
            display_score(current_standings)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                display_board(board)
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                display_board(board)
                break

        if detect_winner(board) == 'Player':
            prompt(f"You win Round {current_standings['Round Number']}!!")
            current_standings['Player Score'] += 1
        elif detect_winner(board) == 'Computer':
            prompt('The computer wins this round!')
            current_standings['Computer Score'] += 1
        else:
            prompt("It's a tie!")

        current_standings['Round Number'] += 1
        time.sleep(2)
        
        if current_standings['Player Score'] == WINNING_NUMBER: #TURN THIS INTO A FUNCTION SINCE IT IS REE
            prompt(f"You are the Grand Winner!")
            play_again = input("Would you like to play again? y/n \n")
            if play_again == 'y':
                reset_scores(current_standings)
            elif play_again == 'n':
                prompt("Thanks for playing!")
                break
                
        elif current_standings['Computer Score'] == WINNING_NUMBER:
            prompt(f"The Computer is the Grand Winner")
            play_again = input("Would you like to play again? y/n \n")
            if play_again == 'y':
                reset_scores(current_standings)
            elif play_again == 'n':
                prompt("Thanks for playing!")
                break

play_tic_tac_toe()