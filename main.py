from player import Player
from hand import Hand
import random

welcome_message = "\t\tWelcome to Blackjack!\n"
players = []

# Customizations:

# Support for playing against AI
#   (AI make pass/hit decisions)
# Support to run simulation games if no human player exists 
# 	i.e. run 100 games with 5 AI players then print winning stats
# 

def init():
	print(welcome_message)
	
	# Get player/s info
	num_human = num_ai = 0
	num_players = int(raw_input("How many players? (Human and AI): "))
	if num_players >= 1:
		num_human = int(raw_input("How many human players?: ".format(num_players)))
	if not num_players == 1:
		num_ai = num_players - num_human
	
	# Play one game unless no human players
	num_games = 1
	if num_human == 0:
		num_games = int(raw_input("How many simulations do you want to run?: "))

	# Init human players
	for p in range(0, num_human):
		player = Player(raw_input("Enter player name: "), False)
		players.append(player)
	# Init AI players
	for p in range(num_human, num_players):
		player = Player()
		player.gen_name()
		players.append(player)
	
	return num_games

def shuffle(hand):
	# Shuffle cards 1337 times just because
	num_cards = len(hand.cards)
	for i in range(0, 1337):
		for c in range(0, num_cards):
			rand_index = random.randint(0, c)
			temp = hand.cards[c]
			hand.cards[c] = hand.cards[rand_index]
			hand.cards[rand_index] = temp

def deal(deck):
	# Deal initial 2 cards to all players
	for player in players:
		for i in range(0, 2):
			card = deck.cards[0]
			player.draw_card(card)
			deck.remove(card)
		player.optimize()

def print_state(with_dealer):
	# Print current state of game
	print
	if with_dealer:
		for player in players:
			print("{0}: {1}  ({2})".format(player.name, str(player.hand), player.score))
	else:
		for player in players:
			if not player.name == "Dealer":
				print("{0}: {1}  ({2})".format(player.name, str(player.hand), player.score))
	print
			
def get_max():
	# Get leading value in current state of game
	max_val = 0
	for player in players:
		if player.name == "Dealer":
			continue
		if player.score > max_val:
			if not player.score > 21:
				max_val = player.score
	return max_val

# Initialize game and config dealer
num_games = init()
players.append(Player("Dealer", True))
dealer = players[len(players)-1]
dealer.live = False

# Start game/s
for game in range(0, num_games):
	# Shuffle deck and deal
	deck = Hand()
	deck.gen_deck()
	shuffle(deck)
	deal(deck)
	
	# Adjust live players to not include dealer
	live_players = len(players) - 1
	
	while not live_players == 0:
		# Print without dealer cards
		if num_games == 1:
			print_state(False)
		
		# Iterate through each player's turn
		for player in players:
			# If player busted/passed don't process
			if not player.live:
				continue
			
			# Process player action (hit or pass)
			max_val = get_max()
			# Hit
			if player.hit(max_val, live_players / len(players)):
				# Draw card
				card = deck.cards[0]
				deck.remove(card)
				player.draw_card(card)
				if num_games == 1:
					print("{0} draws a {1}".format(player.name, card))
				
				# Check for bust
				if not player.live:
					live_players -= 1
					player.busted = True
					if num_games == 1:
						print("{0} busts with a score of {1}\n".format(player.name, player.score))
			# Pass
			else:
				if num_games == 1:
					print("{0} passes".format(player.name))
				player.live = False
				live_players -= 1

	# Print final state and find winner/s
	if num_games == 1:
		print_state(True)
	winners = []
	top_score = 0
	for player in players:
		# Don't process busted player
		if player.busted:
			continue
		
		# Replace top score if greater
		if player.score > top_score:
			top_score = player.score
			winners = []
			winners.append(player)
		# Add to winners if match top score
		elif player.score == top_score:
			winners.append(player)
	
	# Print winner/s		
	for winner in winners:
		winner.num_wins += 1
		if num_games == 1:
			print("{0} wins with a score of {1}".format(winner.name, winner.score))
	
	# Reset all players
	for player in players:
		if not player.name == "Dealer":
			player.live = True
		player.score = 0
		player.busted = False

# Print winning stats
print("\nNumber of games played: {0}".format(num_games))
for player in players:
	print("{0} # of wins: {1}".format(player.name, player.num_wins))
