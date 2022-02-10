import random

card_names = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING' ]
suits = [ 'CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
message_list = ["Place a bet", "Bet too high", "You lost this round as the card is not in between", "Game Over", "The pot is", "Your bank amount is", "Would like you like to make the ace HIGH or LOW", "HIGH", "LOW"]
keep_going = True
pot = []
#card_deck = [ (len(card_names)-1) * [True] for i in range(suits) ]
card_deck = [ ]
num_suits = 4
num_cards_values = 13
num_cards = num_cards_values * num_suits
which_player = False
reset_deck = 4
ante = 20
player_hand = [ ]
bet = 0
num_cards_in_hand = 2
whichMessage = 1


def init_deck(deck_values, num_cards, num_cards_values, num_suits):
    deck_values = [ num_cards_values * [True] for i in range(num_suits) ]
    return deck_values, num_cards
