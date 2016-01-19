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

    long_rank_string_map = ['ACE_LOW', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']
    long_suit_string_map = ["CLUBS","HEARTS","DIAMONDS","SPADES"]
    
    rank_string_map = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit_string_map = ["c","h","d","s"]

    def __init__(self, rank_suit_string):
        """
        Expects a string of the form ranksuit, i.e. As for Ace of spades
        """
        self.rank = Card.rank_string_map.index(rank_suit_string[0])
        self.suit = Card.suit_string_map.index(rank_suit_string[1])

    def __hash__(self):
        return (self.rank*10) + self.suit

    def to_string(self):
        result = Card.rank_string_map[self.rank] + Card.suit_string_map[self.suit]
        return result

        
