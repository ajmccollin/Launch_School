import random
import time
import os

import json
with open('rock_paper_scissors_message.json', 'r') as file:
    MESSAGE = json.load(file)

#THINGS TO ADJUST:
    #Make both 'r' and 'rock' valid inputs, for all choices.
    #json file for instructions on line 32

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'sp': 'spock',
    'l': 'lizard',
}

WINNING_CONDITIONS = {
    'r': ['sc', 'l'],
    'p': ['r', 'sp'],
    'sc': ['p', 'l'],
    'sp': ['r', 'sc'],
    'l': ['sp', 'p'],
}

def prompt(message):
    print(f'==> {message}')

def display_instructions():
    os.system('clear')
    prompt('Scissors cuts Paper and decapitates Lizard!')
    prompt('Paper covers Rock and disproves Spock!')
    prompt('Rock crushes Lizard and crushes Scissors!')
    prompt('Lizard eats Paper and poisons Spock!')
    prompt('Spock smashes Scissors and vaportizes Rock!\n')
    prompt('Beat the Computer in a best of 5 to be crowned the Grand Winner!')
    time.sleep(2)


def display_winner(player, computer):
    if computer in (WINNING_CONDITIONS[player]): #Player loss condition
        player_loss()
    elif (player in WINNING_CONDITIONS[computer]): #Player win condition
        player_win()
    else:
        print("==> It's a tie!", end=' ')

def display_score():
    print(f"The score is {current_standings['Player Score']}:"
          f"{current_standings['Computer Score']}\n")

def player_loss():
    print('==> You lost this round! ', end= '')
    current_standings['Computer Score'] += 1

def player_win():
    print('==> You win this round. ', end= '')
    current_standings['Player Score'] += 1

def display_current_round():
    print(f"==> Round {current_standings['Round Number']}! "
           "Make your selection:")


os.system('clear')
prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
prompt('Would you like the rules to this game? (y/n?)' )
show_rules = input().lower()

while show_rules not in ['y', 'yes', 'n', 'no']:
    prompt(MESSAGE['yes_no'])
    show_rules = input().lower()

if show_rules in ['yes', 'y']:
    display_instructions()

print()
for key, value in VALID_CHOICES.items():
    print(f"==> Enter '{key}' for {value}")
print()

while True: #Loop to decide whether to play again.
    current_standings = {
        'Computer Score' : 0,
        'Player Score' : 0,
        'Round Number' : 1,
    }

    while True:
        time.sleep(.5)
        display_current_round()
        user_choice = input().lower()

        while user_choice not in (VALID_CHOICES):
            prompt(f"Invalid input. "
                   f"Please enter {', '.join(VALID_CHOICES.keys())}")
            user_choice = input().lower()

        computer_choice = random.choice(list(VALID_CHOICES.keys()))
        prompt(f'You chose {VALID_CHOICES[user_choice].capitalize()}. '
               f'The computer chose '
               f'{VALID_CHOICES[computer_choice].capitalize()}.')

        display_winner(user_choice, computer_choice)
        display_score()
        current_standings['Round Number'] += 1

        if current_standings['Player Score'] == 3:
            time.sleep(.5)
            prompt("You're the Grand Winner!!")
            break

        if current_standings['Computer Score'] == 3:
            time.sleep(.5)
            prompt("The computer is the Grand Winner!!")
            break

    prompt('Do you want to play again? (y/n?) ')
    play_again = input().lower()
    while play_again not in ['yes', 'y', 'no', 'n']:
        prompt(MESSAGE['yes_no'])
        play_again = input().lower()

    if play_again[0] == 'n':
        os.system('clear')
        prompt('Thanks for playing!')
        break
    os.system('clear')
