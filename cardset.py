from utils import debug
from collections import Counter

class CardSet():
    """The class that defines all interactions with sets of cards (i.e. hole cards, community cards, etc.). This class is the parent of the game-specific Deck class"""
    def __init__(self, card_set = []):
        self.card_set = card_set

    def add_card(self, card):
        self.card_set.append(card)

    def add_card_set(self, card_set):
        self.card_set.append(card_set)

    def to_string(self):
        for c in self.card_set:
            print c.to_string()

    def most_common_rank(self):
        r = [card.rank for card in self.card_set]
        rank = max(set(r), key=r.count)
        return rank

    def most_common_suit(self):
        s = [card.suit for card in self.card_set]
        suit = max(set(s), key=s.count)
        return suit