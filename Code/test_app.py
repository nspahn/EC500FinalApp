from unittest import TestCase
from strategy import *
from app import *

class Test(TestCase):

    def test_display_quote(self):
        self.assertEqual (test_display_quote(symbol.Upper), (symbol.lower))
        self.assertTrue(test_display_quote(symbol.Upper), (symbol.lower))
        self.assertFalse(test_display_quote(symbol.Upper), (symbol.lower))
    def graph(self):
        self.assertEqual(graph(symbol.Upper), (symbol.lower))
        self.assertTrue(1,1) == 0
        self.assertFalse(1000,1) == 999
    def display_history(self):
        self.assertTrue(data) == quote.history(period=period, interval=interval)
        self.assertFalse(quote == symbol)
    def display_quote(self):
        self.assertFlase(symbol == quote)
        self.assertTrue(quote(symbol) == yf.Ticker(symbol))
    def backTesting(self):
        self.assertTrue(ORCLE) == strategy.cerebro.plot)
        self.assertFalse(cerebro.broker.setcash(100000), cerebro.broker.valuation == 100000)