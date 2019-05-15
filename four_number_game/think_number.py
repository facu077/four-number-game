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
        while not number_found:
            if new_number == 9999:
                new_number = 1000
            else:
                new_number += 1
            # For each result stored we check if the new number pass all the controls
            for result in self.results:
                self.comparator.compare_numbers(result.number, str(new_number))
                if self.comparator.regular != result.regular or self.comparator.good != result.good:
                    number_found = False
                    break
                else:
                    number_found = True
        # Then we try with that new number
        self.guessed_number = str(new_number)


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
