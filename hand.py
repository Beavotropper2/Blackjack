from card import Card

class Hand(object):
    
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        num_cards = len(self.cards)
        return_fmt = ""
        for index in range(0, num_cards):
            return_fmt += str(self.cards[index]) + "\n"
        return return_fmt
                    
    def gen_deck(self):
        rank_size = 13
        suit_size = 4

        for s in range(0, len(Card.SUITS)):
            for r in range(0, len(Card.RANKS)):
                card = Card(Card.RANKS[r], Card.SUITS[s])
                self.cards.append(card)
            
