
class Card(object):
    
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    SUITS = ["Clb", "Dmd", "Hrt", "Spd"]
    
    value = 0
    
    def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
        
        # Set card value
		if self.rank == "Ace":
			self.value = 11
		elif self.rank in ("Jack", "Queen", "King"):
			self.value = 10
		else:
			self.value = int(self.rank)
        
    def __str__(self):
        return self.rank + " of " + self.suit
