import unittest
import think_number


class ThinkNumberTest(unittest.TestCase):

    def setUp(self):
        self.guesser = think_number.Guesser()
        self.guesser.guessed_number = '7234'

    def test_guess_bigger(self):
        # assuming the user thought 8730
        self.guesser.guess(1, 1)
        self.assertEqual(self.guesser.guessed_number, '7301')
        self.guesser.guess(3, 0)
        self.assertEqual(self.guesser.guessed_number, '8037')
        self.guesser.guess(2, 2)
        self.assertEqual(self.guesser.guessed_number, '8730')

    def test_guess_lower(self):
        # assuming the user thought 1358
        self.guesser.guess(1, 0)
        self.assertEqual(self.guesser.guessed_number, '8012')
        self.guesser.guess(2, 0)
        self.assertEqual(self.guesser.guessed_number, '9103')
        self.guesser.guess(2, 0)
        self.assertEqual(self.guesser.guessed_number, '1358')



if __name__ == "__main__":
    unittest.main()
