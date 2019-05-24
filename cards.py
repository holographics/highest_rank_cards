from collections import OrderedDict
import numpy as np

RANKS = [str(i) for i in range(2, 11) + list('JQKA')]         
SUITS = ['hearts', 'spades', 'clubs', 'diamonds']

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s%s' % (self.rank, self.suit[0])
        
def get_output(cards):
    ranks = [card.rank for card in cards]
    counts = {rank: ranks.count(rank) for rank in list(set(ranks))}
    highest_rank = OrderedDict(sorted(counts.items(), key=lambda items: items[1], reverse=1)).keys()[0]
    return sorted( [str(card) for card in cards if card.rank == highest_rank] )

cards = [Card(suit, rank) for suit in SUITS for rank in RANKS] 
    
rand_range = list(set(np.random.uniform(low=1, high=52, size=25).astype(int)))[:7]
rand_cards = [cards[rand_int] for rand_int in rand_range]
    
result = get_output(random_cards)
print 'result: %s' % result
