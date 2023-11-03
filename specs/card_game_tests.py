import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def test_can_check_for_ace(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        self.assertEqual(CardGame.check_for_ace(CardGame, card1), False)

    def test_can_find_highest_card(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        self.assertEqual(CardGame.highest_card(self, card1, card2), card1)

    def test_can_cadd_cards_total(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        self.assertEqual(
            CardGame.cards_total(self, [card1, card2]), "You have a total of3"
        )
