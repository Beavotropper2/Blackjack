from card import Card

# A Hand has a list of Cards
class Hand(object):
    
	def __init__(self):
		self.cards = []
        
	def __str__(self):
		return_fmt = ""
		for card in self.cards:
			return_fmt += str(card).ljust(12)
		return return_fmt
    
	def add(self, card):
		self.cards.append(card)
		
	def remove(self, card):
		self.cards.remove(card)
		             
	def gen_deck(self):
		rank_size = 13
		suit_size = 4

		for s in range(0, len(Card.SUITS)):
			for r in range(0, len(Card.RANKS)):
				card = Card(Card.RANKS[r], Card.SUITS[s])
				self.cards.append(card)
