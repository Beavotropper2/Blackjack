from hand import Hand

class Player(object):
    
	def __init__(self, player):
		self.player = player
		self.hand = Hand()
        
	def draw_card(card):
		self.hand.cards.append(card)
		
	def get_card(index):
		card = self.hand.cards[index]
		return card
