import unittest
from utils import debug
from cardset import CardSet
from card import Card

class CardSetTest(unittest.TestCase):

    def test_most_common_rank(self):
        sample_set = CardSet()
        sample_set.add_card(Card('5s'))
        sample_set.add_card(Card('5c'))
        sample_set.add_card(Card('6h'))
        sample_set.add_card(Card('Jh'))
        result = sample_set.most_common_rank()
        print(sample_set.to_string())
        self.assertEqual(result, Card.FIVE)

    def test_most_common_suit(self):
        sample_set = CardSet()
        sample_set.add_card(Card('5s'))
        sample_set.add_card(Card('6s'))
        sample_set.add_card(Card('7h'))
        sample_set.add_card(Card('Jc'))
        result = sample_set.most_common_suit()
        print(sample_set.to_string())
        self.assertEqual(result, Card.SPADES)

if __name__ == '__main__':
    unittest.main()
