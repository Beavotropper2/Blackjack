class Card(object):
    
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + " of " + self.suit
        
