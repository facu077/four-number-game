import random


class Thinker:
    def __init__(self):
        self.number = self.generate_number()

    def compare_numbers(self, user_input):
        result = Result()

        # We need backup for the values since we are going to modify them
        thinker_number = self.number
        user_number = user_input

        # First we go through the two string at the same time and remove the matches
        for thinker_digit, user_digit in zip(self.number, user_input):
            if thinker_digit is user_digit:
                result.good += 1
                user_number = user_number.replace(user_digit, '', 1)
                thinker_number = thinker_number.replace(thinker_digit, '', 1)

        # Then we go through the rest of the string looking for regulars and removing the digit when we find one
        for digit in user_number:
            if thinker_number.find(digit) is not -1:
                result.regular += 1
                thinker_number = thinker_number.replace(digit, '', 1)

        return result

    @staticmethod
    def generate_number():
        return str(random.randint(1000, 9999))


class Result:
    good: int
    regular: int

    def __init__(self, good=0, regular=0):
        self.good = good
        self.regular = regular


def main():
    thinker = Thinker()
    result = Result()

    while result.good is not 4:
        print('Please enter a four digit number: ')
        number = input()
        if len(number) is not 4:
            print('Wrong number. Number should have four digits')
        else:
            result = thinker.compare_numbers(number)
            print('Good: ' + str(result.good) + ' Regular: ' + str(result.regular))
    print('Game over: You have found the number! It was ' + thinker.number)


if __name__ == "__main__":
    main()
