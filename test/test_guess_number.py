import unittest

from four_number_game import guess_number


class GuessNumberTest(unittest.TestCase):

    # TODO
    def setUp(self):
        self.thinker = guess_number.Thinker()
        self.thinker.number = '5316'


if __name__ == "__main__":
    unittest.main()
