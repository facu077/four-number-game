from lib import utilities


class Guesser:
    def __init__(self):
        self.guessed_number = utilities.generate_number()
        self.results = []
        self.comparator = utilities.Comparator()

    def guess(self, regular, good):
        # We store the user answer in a list of results objects
        last_result = Result(self.guessed_number, good, regular)
        self.results.append(last_result)

        new_number = int(self.guessed_number)
        number_found = False
        # If the user enters a wrong input the 'while' will be stuck forever
        # so we are going to use 'infinite_loop_control' to prevent it
        infinite_loop_control = 0
        while not number_found:
            infinite_loop_control += 1
            # We need to check that the new number doesn't have any duplicated digit
            number_with_duplicates = True
            while number_with_duplicates:
                if new_number == 9876:
                    new_number = 1234
                else:
                    new_number += 1
                number_with_duplicates = self.has_duplicates(str(new_number))
            # For each result stored we check if the new number pass all the controls
            for result in self.results:
                self.comparator.compare_numbers(result.number, str(new_number))
                if self.comparator.regular != result.regular or self.comparator.good != result.good:
                    number_found = False
                    break
                else:
                    number_found = True
            if infinite_loop_control > 9876:
                # After a full check of all the possible number we still can't find a new 'guessed_number'
                # That happens when the user enters a wrong input, so we need to reset the conditions
                self.results = []
                print('It seems that you have entered an incorrect value. Resetting the inputs')
                break
        # Then we try with that new number
        self.guessed_number = str(new_number)

    @staticmethod
    def has_duplicates(value):
        for char in value:
            count = value.count(char)
            if count > 1:
                return True
        return False


# Class used to save the results
class Result:
    def __init__(self, number='', good=0, regular=0):
        self.number = number
        self.good = good
        self.regular = regular


def main():
    guesser = Guesser()
    number_found = False

    while not number_found:
        answer = input('Is your number ' + guesser.guessed_number + '? ')
        if answer == 'yes' or answer == 'y':
            print('Game over: Your number was: ' + guesser.guessed_number)
            number_found = True
        elif answer == 'no' or answer == 'n':
            try:
                regular = int(input('Regular numbers: '))
                good = int(input('Good numbers: '))
            except ValueError:
                print('Value should be an int')
                continue
            else:
                guesser.guess(regular, good)
        else:
            print('Answer should be [y]es or [n]o')


if __name__ == "__main__":
    main()
