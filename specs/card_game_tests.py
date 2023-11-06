import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        cardGame = CardGame()

    def test_can_check_for_ace(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        cardGame = CardGame()
        self.assertEqual(cardGame.check_for_ace(card1), False)

    def test_can_find_highest_card(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        cardGame = CardGame()
        self.assertEqual(cardGame.highest_card(card1, card2), card1)

    def test_can_cadd_cards_total(self):
        card1 = Card("Hearts", 2)
        card2 = Card("Hearts", 1)
        cardGame = CardGame()
        self.assertEqual(cardGame.cards_total([card1, card2]), "You have a total of3")
