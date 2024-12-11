import random
import time
import os

import json
with open('rock_paper_scissors_message.json', 'r') as file:
    MESSAGE = json.load(file)

VALID_CHOICES = {'r': 'rock',
                 'p': 'paper',
                 'sc': 'scissors',
                 'sp': 'spock',
                 'l': 'lizard',
                 }


def prompt(message):
    print(f'==> {message}')

def yes_or_no(user_selection): #Validates that user input is either y or n
    while True:
        if user_selection.startswith('n') or user_selection.startswith('y'):
            break
        prompt("Please enter 'y' or 'n'.")
        user_selection = input()

def display_winner(player, computer, iteration): #Iteration is number of rounds
    if ((player == 'r' and computer == 'sc') or
        (player == 'r' and computer == 'l') or
        (player == 'p' and computer == 'r') or
        (player == 'p' and computer == 'sp') or
        (player == 'sc' and computer == 'p') or
        (player == 'sc' and computer == 'l') or
        (player == 'sp' and computer == 'r') or
        (player == 'sp' and computer == 'sc') or
        (player == 'l' and computer == 'sp') or
        (player == 'l' and computer == 'p')):
        prompt(f'You win round {iteration}!\n')
    elif ((computer == 'r' and player == 'sc') or
        (computer == 'r' and player == 'l') or
        (computer == 'p' and player == 'r') or
        (computer == 'p' and player == 'sp') or
        (computer == 'sc' and player == 'p') or
        (computer == 'sc' and player == 'l') or
        (computer == 'sp' and player == 'r') or
        (computer == 'sp' and player == 'sc') or
        (computer == 'l' and player == 'sp') or
        (computer == 'l' and player == 'p')):
        prompt(f'You lose round {iteration}!\n')
    else:
        prompt(f'Round {iteration} is a tie!\n')

os.system('clear')
prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
prompt('Would you like the rules to this game? (y/n?)' )
display_instructions = input().lower()
yes_or_no(display_instructions)

if display_instructions == 'y':
    os.system('clear')
    prompt('Scissors cuts Paper and decapitates Lizard!\n'
           'Paper covers Rock and disproves Spock!\n'
           'Rock crushes Lizard and crushes Scissors!\n'
           'Lizard eats Paper and poisons Spock!\n'
           'Spock smashes Scissors and vaportizes Rock!\n')
    time.sleep(2)

while True: #Loop to decide whether to play again.
    prompt('Please enter:') #Prints valid options for user to choose from.
    for key, value in VALID_CHOICES.items():
        print(f"'{key}' for {value}")
    print()

    round_number = 1
    while round_number <= 5:
        prompt(f"Round {round_number}! "
               f"Enter {', '.join(VALID_CHOICES.keys())}")
        user_choice = input().lower()

        while user_choice not in VALID_CHOICES:
            prompt(f"Invalid input. "
                   f"Please enter {', '.join(VALID_CHOICES.keys())}")
            user_choice = input()

        computer_choice = random.choice(list(VALID_CHOICES.keys()))
        prompt(f'You chose {VALID_CHOICES[user_choice].capitalize()}. '
               f'The computer chose '
               f'{VALID_CHOICES[computer_choice].capitalize()}.')

        display_winner(user_choice, computer_choice, round_number)
        round_number += 1


    prompt('Do you want to play again? (y/n?) ')
    play_again = input().lower()
    yes_or_no(play_again)

    if play_again[0] == 'n':
        os.system('clear')
        prompt('Thanks for playing!')
        break
    os.system('clear')