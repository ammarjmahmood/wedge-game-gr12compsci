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

# init_deck(card_deck, num_cards, num_cards_values, num_suits)
    
def init_pot(pot):
    pot = [ 500, 500, 1000 ]

def get_a_card( deck_values, num_suits, num_cards ):
    suit_choice = random.randint(0, num_suits)
    card_choice = random.randint(0, num_cards)
    while deck_values[suit_choice][card_choice] == False:
        suit_choice = random.randint(0, num_suits)
        card_choice = random.randint(0, num_cards)
    deck_values[suit_choice][card_choice] = False
    return( suit_choice, card_choice )

def get_a_hand(card_deck, player_hand, num_cards_in_hand):
    player_hand = []
    for i in range(num_cards_in_hand):
        card_picked, suit_picked = get_a_card(card_deck, num_suits - 1 , num_cards -1)
    player_hand = [ [card_picked, suit_picked] [card_picked, suit_picked] ]
    return player_hand

def what_bet(pot, ante, bet, message_list, WhichMessage):
    starting_placeVal = 0
    ending_placeVal = pot[2] # top value is the amount of pot
    #print( message_list[ whichMessage ] )
    validNum = int( input())
    keepGoing = ( validNum < starting_placeVal ) or ( validNum > ending_placeVal )
    while keepGoing:
         #print( message_list[ whichMessage + 1 ] )
         validNum = int( input())
         keepGoing = ( validNum < starting_placeVal ) or ( validNum > ending_placeVal )
    return validNum

def change_ace(player_hand):
    #print(message_list[whichMessage + 3])
    ace_value = str(input()).upper()
    if ace_value == message_list[whichMessage + 6]:
        # high
        pass
    

def payout(pot, bet, player_hand):
    pass

def switch_player(which_player):
    pass

def quit(pot):
    pass


card_picked, suit_picked = get_a_card(card_deck, num_suits - 1 , num_cards -1)

while keep_going:
    pass

