from hand import Hand
import linecache
import random

# used following link for names.txt
# http://stackoverflow.com/questions/1803628/raw-list-of-person-names

# A Player has a Hand of Cards
class Player(object):
	
	score = 0
	num_wins = 0
    
	def __init__(self, name="", ai=True):
		self.name = name
		self.hand = Hand()
		self.live = True
		self.busted = False
		self.ai = ai
		
	def optimize(self):	
		# Optimize Ace value for player score
		for card in self.hand.cards:
			if self.score > 21:
				if card.value == 11:
					card.value = 1
					self.score -= 10
        
	def draw_card(self, card):
		self.hand.add(card)
		self.score += card.value
		self.optimize()
		if self.score > 21:
			self.live = False
		
	def get_card(self, index):
		card = self.hand.cards[index]
		return card
		
	def gen_name(self):
		# Use names.txt to generate random AI name
		line = random.randint(100, 4000)
		self.name = linecache.getline('names.txt', line)
		self.name = self.name.split()[0]

	def hit(self, max_val, live_players):
		# Human determines decision
		if not self.ai:
			choice = raw_input("{0}, do you want a hit? (yes/no): ".format(self.name))
			if choice in ("yes", "y", "yeah", "yea"):
				return True
			elif choice in("no", "n", "nope"):
				return False
			else:
				return hit(self, max_val, live_players)
		# AI determines decision
		else:
			# In lead
			if self.score == max_val:
				if self.score >= 19:
					return False
				else:
					return True
			# Not in lead
			else:
				if self.score < 11:
					return True
						
				if self.score < 18:
					hit_chance = random.randint(0, 5)
					if hit_chance > 1:
						return True
					else:
						return False
				else:
					return False
			
			
