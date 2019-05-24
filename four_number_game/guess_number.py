from lib import utilities


class Thinker:
    def __init__(self):
        self.number = utilities.generate_number()
        self.comparator = utilities.Comparator()

    def compare_numbers(self, user_input):
        # With the comparator object we compare the pc number with the user one, and store the result of good/ regulars
        self.comparator.compare_numbers(self.number, user_input)


def main():
    thinker = Thinker()

    while thinker.comparator.good != 4:
        number = input('Please enter a four digit number: ')
        if len(number) != 4:
            print('Wrong number. Number should have four digits')
        else:
            thinker.compare_numbers(number)
            print('Good: ' + str(thinker.comparator.good) + ' Regular: ' + str(thinker.comparator.regular))
    print('Game over: You have found the number! It was ' + thinker.number)


if __name__ == "__main__":
    main()
