import unittest
from utils import debug
from cardset import CardSet
from card import Card

class CardSetTest(unittest.TestCase):

    def test_most_common_rank(self):
        sample_set = CardSet()
        sample_set.add_card(Card(Card.FIVE, Card.SPADES))
        sample_set.add_card(Card(Card.FIVE, Card.CLUBS))
        sample_set.add_card(Card(Card.SEVEN, Card.SPADES))
        sample_set.add_card(Card(Card.JACK, Card.HEARTS))
        result = sample_set.most_common_rank()
        print(sample_set.to_string())
        self.assertEqual(result, Card.FIVE)

    def test_most_common_suit(self):
        sample_set = CardSet()
        sample_set.add_card(Card(Card.FIVE, Card.SPADES))
        sample_set.add_card(Card(Card.SIX, Card.SPADES))
        sample_set.add_card(Card(Card.SEVEN, Card.SPADES))
        sample_set.add_card(Card(Card.JACK, Card.HEARTS))
        result = sample_set.most_common_suit()
        print(sample_set.to_string())
        self.assertEqual(result, Card.SPADES)

if __name__ == '__main__':
    unittest.main()