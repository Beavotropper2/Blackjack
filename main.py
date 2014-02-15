from player import Player
import random

welcome_message = "\t\t\tWelcome to Blackjack!\n"
num_players = 1
players = []

def init():
	print(welcome_message)
	num_players = int(raw_input("How many players? (1 - 7): "))
	for p in range(0, num_players):
		player = Player(raw_input("Enter player name: "))
		players.append(player)

def shuffle(hand):
	num_cards = len(hand.cards)
	for i in range(0, 1337):
		for c in range(0, num_cards):
			rand_index = random.randint(0, c)
			temp = hand.cards[c]
			hand.cards[c] = hand.cards[rand_index]
			hand.cards[rand_index] = temp

def deal(hand):
	for p in range(0, num_players):
		player = players[p]
		for i in range(0, 2):
			card = hand.cards[0]
			player.draw_card(card)
			hand.remove(card)

def print_state():
	print(num_players)
	for p in range(0, num_players):
		player = players[p]
		card_one = player.get_card(0)
		card_two = player.get_card(1)
		print("{0}: {1} \t {2} \t {3}".format(player, card_one, card_two, score))

# Main

# Get game setup
init()

# Create dealer/deck and shuffle
dealer = Player("Dealer")
dealer.hand.gen_deck()
shuffle(dealer.hand)
#print(dealer.hand)

# Deal cards
deal(dealer.hand)

# Start game/s
done = 0
while not done:
	print_state()
	done = 1
