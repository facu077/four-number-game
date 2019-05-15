import unittest

from four_number_game.lib import utilities


class UtilitiesTest(unittest.TestCase):

    def setUp(self):
        self.comparator = utilities.Comparator()

    def test_comparator_good(self):
        self.comparator.compare_numbers('1234', '8264')
        self.assertEqual(self.comparator.good, 2)
        self.assertEqual(self.comparator.regular, 0)

    def test_comparator_regular(self):
        self.comparator.compare_numbers('1234', '4389')
        self.assertEqual(self.comparator.good, 0)
        self.assertEqual(self.comparator.regular, 2)

    def test_comparator_both(self):
        self.comparator.compare_numbers('1234', '1249')
        self.assertEqual(self.comparator.good, 2)
        self.assertEqual(self.comparator.regular, 1)

    def test_comparator_none(self):
        self.comparator.compare_numbers('1234', '7698')
        self.assertEqual(self.comparator.good, 0)
        self.assertEqual(self.comparator.regular, 0)


if __name__ == "__main__":
    unittest.main()
