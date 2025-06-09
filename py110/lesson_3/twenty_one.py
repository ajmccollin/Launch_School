'''
Twenty One

This module is a very basic variation on the classic game of Blackjack.
In this game, a deck of cards is shuffled and then dealt to the dealer (the
copmuter) then to the player. Based on typical scoring of Blackjack, if the 
player or dealer goes over 21, they lose. Otherwise, the highest scorer wins.

Author: jm
Date: June 2025
'''
import random
import time
import os

DECK_OF_CARDS = {
    'Spades': {2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'},
    'Clubs': {2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'},
    'Hearts': {2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'},
    'Diamonds': {2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'},
}

FACE_CARDS = {
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': [1, 11],
}

def prompt(message):
    ''' Prints message with a prompter for improved clarity '''
    print(f"==> {message}")

def shuffle_deck(deck):
    ''' 
    Stores original deck in list and then uses built in shuffle function
    to randomize the deck.
    '''
    shuffled_deck = []
    for values in deck.values():
        for card in values:
            shuffled_deck.append(card)
    random.shuffle(shuffled_deck)
    return shuffled_deck

def sum_of_cards(current_hand):
    total_hand = 0
    ace_count = 0
    for card in current_hand:
        if card in range(1, 11):
            total_hand += card
        elif card in FACE_CARDS and card != 'Ace':
            total_hand += 10
        elif card == 'Ace':
            ace_count += 1

    while ace_count != 0:
        if (total_hand + 11) <= 21:
            total_hand += 11
            ace_count -= 1
        else:
            total_hand += 1
            ace_count -= 1

    return total_hand

def busted(current_hand):
    return sum_of_cards(current_hand) > 21

def deal_starting_hands(deck, hands, cards_in_hand=2):
    for _ in range(cards_in_hand):
        for player in hands:
            hands[player].append(deck.pop(0))

def player_turn(deck, current_hand):
    player_total_hand = sum_of_cards(current_hand['Player'])
    prompt(f"Your current hand is equal to {player_total_hand}.")
    time.sleep(1)
    while True:
        try:
            keep_going = input('==> Would you like to hit or stay? ')
            while keep_going.lower() not in ['hit', 'stay']:
                keep_going = input('==> Please choose to hit or stay: ')
        except AttributeError:
            keep_going = input('==> Please choose to hit or stay: ')
        if keep_going == 'stay' or busted(current_hand['Player']):
            break

        current_hand['Player'].append(deck.pop(0))
        prompt(f"You drew: {current_hand['Player'][-1]}")
        time.sleep(1)

        player_total_hand = sum_of_cards(current_hand['Player'])
        prompt(f"Your current hand is equal to {player_total_hand}.")
        time.sleep(1)

        if busted(current_hand['Player']):
            break

    if busted(current_hand['Player']):
        prompt('You went over 21! You lose!')
        time.sleep(1)
        print()
    else:
        prompt(f"You chose to stay at {player_total_hand}.\n")

def dealer_turn(deck, current_hand):
    prompt(f"The dealer's hand contains {current_hand['Dealer'][0]} and "
           f"{current_hand['Dealer'][1]}.")
    time.sleep(1)
    dealer_total_hand = sum_of_cards(current_hand['Dealer'])
    prompt(f"The dealer's hand is equal to {dealer_total_hand}")
    time.sleep(1)

    while dealer_total_hand < 17:
        current_hand['Dealer'].append(deck.pop(0))
        prompt(f"The dealer drew: {current_hand['Dealer'][-1]}")
        time.sleep(1)
        dealer_total_hand = sum_of_cards(current_hand['Dealer'])
        prompt(f"The dealer's hand is equal to {dealer_total_hand}. \n")
        time.sleep(1)

    if busted(current_hand['Dealer']):
        prompt('The dealer went over 21! You win!!')
    else:
        prompt("The dealer chooses to stay \n")

def compare_hands(current_hand):
    prompt(f"Your hand is equal to {sum_of_cards(current_hand['Player'])}.")
    time.sleep(1)
    prompt(f"The dealer's hand is equal to "
           f"{sum_of_cards(current_hand['Dealer'])}.")
    time.sleep(1)

    if (sum_of_cards(current_hand['Dealer']) >
        sum_of_cards(current_hand['Player'])):
        prompt('The dealer wins!')
    elif (sum_of_cards(current_hand['Player']) >
          sum_of_cards(current_hand['Dealer'])):
        prompt('You win!')
    else:
        prompt("It's a tie!")

def play_game():
    while True:
        os.system('clear')
        shuffled_cards = shuffle_deck(DECK_OF_CARDS)
        current_hand = {
            'Dealer': [],
            'Player': [],
        }

        deal_starting_hands(shuffled_cards, current_hand)

        prompt(f"Dealer has: {current_hand['Dealer'][0]} and an unknown card.")
        time.sleep(1)
        prompt(f"You have: {current_hand['Player'][0]} and "
            f"{current_hand['Player'][1]}")
        time.sleep(1)

        player_turn(shuffled_cards, current_hand)
        if not busted(current_hand['Player']):
            dealer_turn(shuffled_cards, current_hand)
        if not(busted(current_hand['Player']) or busted(current_hand['Dealer'])):
            compare_hands(current_hand)

        try:
            play_again = input("==> Would you like to play again? (y/n) ")
            while play_again.lower() not in ['y', 'yes', 'n', 'no']:
                play_again = input('==> Please enter yes or no. (y/n) ')
        except AttributeError:
            play_again = input('Please enter yes or no (y/n) ')
        if play_again.lower() in ['n', 'no']:
            os.system('clear')
            prompt('Thanks for playing!!')
            break

play_game()
