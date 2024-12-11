import random
import time
import os

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer, round):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'spock' and computer == 'rock') or
        (player == 'spock' and computer == 'scissors') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper')):
        prompt(f'You win round {round}!')
    elif ((computer == 'rock' and player == 'scissors') or
        (computer == 'rock' and player == 'lizard') or
        (computer == 'paper' and player == 'rock') or
        (computer == 'paper' and player == 'spock') or
        (computer == 'scissors' and player == 'paper') or
        (computer == 'scissors' and player == 'lizard') or
        (computer == 'spock' and player == 'rock') or
        (computer == 'spock' and player == 'scissors') or
        (computer == 'lizard' and player == 'spock') or
        (computer == 'lizard' and player == 'paper')):
        prompt(f'You lose round {round}!')
    else:
        prompt(f'Round {round} is a tie!')

os.system('clear')
prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
prompt('Would you like the rules to this game?' )
while True:
    round_number = 1
    while round_number <= 5:
        prompt(f"Round {round_number}! Choose {', '.join(VALID_CHOICES)}.")
        user_choice = input()

        while user_choice not in VALID_CHOICES:
            prompt(f"Invalid input. Please enter {', '.join(VALID_CHOICES)}")
            user_choice = input()

        computer_choice = random.choice(VALID_CHOICES)
        prompt(f'You chose {user_choice}. ' 
               f'The computer chose {computer_choice}.')

        display_winner(user_choice, computer_choice, round_number)
        round_number += 1


    prompt('Do you want to play again? (y/n?) ')
    play_again = input().lower()

    while True:
        if play_again.startswith('n') or play_again.startswith('y'):
            os.system('clear')
            break
        prompt("Please enter 'y' or 'n'.")
        play_again = input().lower()

    if play_again[0] == 'n':
        prompt('Thanks for playing!')
        break


#Scissors beats Paper
#Scissors beats Lizard
#Paper beats Rock
#Paper beats Spock
#Rock beats Lizard
#Rock beats Scissors
#Lizard Beats Spock
#Lizard Beats Paper
#Spock beats Rock
#Spock beats Scissors