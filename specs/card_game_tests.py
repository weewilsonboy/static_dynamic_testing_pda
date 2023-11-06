import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardGame = CardGame()
        self.card1 = Card("Hearts", 2)
        self.card2 = Card("Hearts", 1)

    def test_can_check_for_ace(self):
        self.assertEqual(self.cardGame.check_for_ace(self.card1), False)

    def test_can_find_highest_card(self):
        self.assertEqual(self.cardGame.highest_card(self.card1, self.card2), self.card1)

    def test_can_cadd_cards_total(self):
        self.assertEqual(
            self.cardGame.cards_total([self.card1, self.card2]), "You have a total of3"
        )
