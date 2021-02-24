import random

# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	# Prints out card in form of ____ of ____ ex: Seven of Hearts
	def __str__(self):
		return self.rank + " of " + self.suit

class Deck():
	def __init__(self):
		self.deck = [] # Deck is empty at first
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank)) # Use card class to append, gives list of 52 Card classes

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return "The deck has: " + deck_comp

	def shuffle(self):
		random.shuffle(self.deck) # Shuffles the deck list

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:
	def __init__(self):
		self.cards = [] # Person starts with no cards in their hand
		self.value = 0 # Value is also 0 because no cards in hand to start
		self.aces = 0 # Keep track of aces

	def add_card(self, card):
		self.cards.append(card) # Card is from Deck.deal()
		self.value += values[card.rank] 

		# Track aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		# Loop runs if self.value > 21 and there is an ace in player's hand
		# In this case, ace should be a 1 instead of an 11
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

class Chips():
	def __init__(self, total = 100):
		self.total = total # Value can be defaulted to 100 or set by user input
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

# User inputs number of chips they would like to bet
def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry, please provide an integer")
		else:
			if chips.bet > chips.total:
				print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
			else:
				break

# Adds a single card to a deck
def hit(deck, hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()

# Prompts player to hit or stand
def hit_or_stand(deck, hand):
	global playing

	while True:
		x = input('Hit or Stand? Enter h or s')
		if x[0].lower() == 'h': # Using x[0] grabs first character of string, adjusts for communication errors
			hit(deck, hand)
		elif x[0].lower() == 's':
			print("Player stands. Dealer's Turn")
			playing = False
		else:
			print("Sorry, I did not understand that, Please enter h or s only!")
			continue
		break

# Dealer's first card is hidden and player's cards are visible
def show_some(player, dealer):
	print("Dealer's Hand:")
	print("One card hidden!")
	print(dealer.cards[1])
	print("\nPlayer's Hand:")
	for card in player.cards:
		print(card)

# All cards for dealer and player are visible
def show_all(player, dealer):
	print("Dealer's Hand:")
	for card in dealer.cards:
		print(card)
	print ("\nPlayer's Hand:")
	for card in player.cards:
		print(card)

# Game outcomes
def player_busts(player, dealer, chips):
	print("Player busts!")
	chips.lose_bet()

def player_wins(player, dealer, chips):
	print("Player wins!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("Player wins! Dealer busted!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print("Dealer wins!")
	chips.lose_bet()

def push(player, dealer):
	print("Dealer and player tie! It's a push")

while True:
	# Welcoming statement
	print("WELCOME TO BLACKJACK")

	# Create deck, shuffle deck, and deal 2 cards to player/dealer
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Player chips
	player_chips = Chips()

	# Get bet from player
	take_bet(player_chips)

	# Show cards using show_some (because game has just started)
	show_some(player_hand, dealer_hand)

	while playing:
		# Ask player to hit or stand
		hit_or_stand(deck, player_hand)

		# Show cards again, but still keep dealer's first hidden
		show_some(player_hand, dealer_hand)

		# Check to see if player has busted
		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)
			break

	# Check to see if player has not busted, play dealer's hand until dealer reaches 17 (soft 17 rule)
	if player_hand.value <= 21:
		while dealer_hand.value < 17:
			hit(deck, dealer_hand)

		# Show all cards
		show_all(player_hand, dealer_hand)

		# End game scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand, dealer_hand)

		# Let player know how many chips remain
		print('\n Player total chips are at: {}'.format(player_chips.total))

		# Ask to play again
		new_game = input("Would you like to play another hand? y/n ")

		if new_game[0].lower() == 'y':
			playing = True
			continue
		else:
			print("Thank you for playing!")
			break