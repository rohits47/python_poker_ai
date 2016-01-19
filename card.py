class Card():
    """The card class defines all individual card operations"""

    """ Rank and suit constants"""
    ACE = 13
    KING = 12
    QUEEN = 11
    JACK = 10
    TEN = 9
    NINE = 8
    EIGHT = 7
    SEVEN = 6
    SIX = 5
    FIVE = 4
    FOUR = 3
    THREE = 2
    TWO = 1
    ACE_LOW = 0

    CLUBS = 0
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3

    rank_string_map = ['ACE_LOW', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']
    suit_string_map = ["CLUBS","HEARTS","DIAMONDS","SPADES"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __hash__(self):
        return (self.rank*10) + self.suit

    def to_string(self):
        result = Card.rank_string_map[self.rank] + " of " + Card.suit_string_map[self.suit]
        return result

        
