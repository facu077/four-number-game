import random


class Comparator:
    def __init__(self):
        self.regular = 0
        self.good = 0

    def compare_numbers(self, first_number, second_number):
        self.regular = 0
        self.good = 0

        # We are going to use lists since is more easy to manipulate
        first_number_list = list(first_number)
        second_number_list = list(second_number)

        # First we go through the two numbers at the same time
        # and remove the matches from the lists to prevent duplicates
        for first_digit, second_digit in zip(first_number, second_number):
            if first_digit == second_digit:
                self.good += 1
                first_number_list.remove(first_digit)
                second_number_list.remove(first_digit)

        # Then we go through the rest of the list looking for regulars removing when found one to prevent duplicates
        for digit in first_number_list:
            if digit in second_number_list:
                self.regular += 1
                second_number_list.remove(digit)


def generate_number():
    number = '0'
    # We have to check that the numbers doesn't start with 0
    while number[0] == '0':
        number = ''.join(random.sample("0123456789", 4))
    return number
