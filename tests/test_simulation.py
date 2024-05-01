import unittest
from pythonblackjack import Simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.sim = Simulation()

    def test_startGame(self):
        # Test startGame method when user enters 1 (knows how to play)
        with unittest.mock.patch('builtins.input', return_value="1"):
            self.sim.startGame()
            self.assertTrue(self.sim.isGameInPlay())

        # Test startGame method when user enters 0 (needs instructions)
        with unittest.mock.patch('builtins.input', side_effect=["0", "1"]):
            self.sim.startGame()
            self.assertTrue(self.sim.isGameInPlay())

    def test_deal(self):
        # Test deal method to ensure correct dealerTotal and playerTotal are generated
        with unittest.mock.patch('builtins.print') as mock_print:
            with unittest.mock.patch('random.randint', side_effect=[10, 5, 7, 8]):
                self.sim.deal()
                expected_output = [
                    unittest.mock.call("This is the dealer's first card:", 10),
                    unittest.mock.call("This is your hand:"),
                    unittest.mock.call("Card 1:", 5),
                    unittest.mock.call("Card 2:", 7),
                    unittest.mock.call("This is the dealer's first card:", 10),
                    unittest.mock.call("This is your hand:"),
                    unittest.mock.call("Card 1:", 5),
                    unittest.mock.call("Card 2:", 7)
                ]
                mock_print.assert_has_calls(expected_output)

if __name__ == '__main__':
    unittest.main()
