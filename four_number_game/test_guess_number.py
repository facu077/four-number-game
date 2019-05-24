import unittest
import guess_number


class GuessNumberTest(unittest.TestCase):

    def setUp(self):
        self.thinker = guess_number.Thinker()
        self.thinker.number = '5316'

    def test_thinker(self):
        self.thinker.compare_numbers('1387')
        self.assertEqual(self.thinker.comparator.good, 1)
        self.assertEqual(self.thinker.comparator.regular, 1)


if __name__ == "__main__":
    unittest.main()
