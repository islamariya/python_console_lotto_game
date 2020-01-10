import random

from players import Dealer, Player
from settings import number_names


class Raffle(object):
    """This class represents a game from begging to the end. It inits instance of Dealer and Player classes,
    list of unique numbers from 1 to 90, counts of rounds played, list of selected numbers and flag is_game_over.
    Methods of this class includes:
    - random selection of a number for a round,
    - steps that need to be done to play one round of a game,
    - evaluation is game is over,
    - printout to console information about selected number, which includes number of a round played, selected number
    and a "funny" name of this number,
    - printout a game-over message.
    """

    def __init__(self):
        self.my_card = Player()
        self.comp_card = Dealer()
        self.qt_rounds_played = 0
        self.numbers_left = list(range(1, 91))
        self.numbers_played = []
        self.is_game_over = False

    def number_selection(self):
        """This method selects a random number from the list of available for this game. Every time it "shakes" or
        shuffle the list to make the choice more random. To maintain the uniqueness selected number is removed from
        list of available. It also keep tracking the qt of rounds played and updates list of numbers_played.
        :return: number: int
        """
        random.shuffle(self.numbers_left)
        try:
            self.number = self.numbers_left.pop()
            self.numbers_played.append(self.number)
            self.qt_rounds_played += 1
        except IndexError:
            print("Боченков не осталось!")
            self.number = None
        return self.number

    def print_selected_number(self):
        """Prints to console selected number and info about qt numbers left in pretty way.
        """
        print()
        print(f"РАУНД {self.qt_rounds_played}")
        try:
            print(f"Выпало число: {self.number}! {str(number_names[self.number])}")
        except KeyError:
            print(f"Выпало число: {self.number}!")
        print(f"Осталось {len(self.numbers_left)} боченков \n")

    def play_a_round(self):
        """This method defines sequence of needed methods in every round of the game. This sequence is repeated untill
        the game is over.
        """
        number = self.number_selection()
        self.print_selected_number()
        self.comp_card.print_a_card()
        self.my_card.print_a_card()
        self.comp_card.find_the_num_in_card(number)
        self.my_card.underline_number(number, self)
        self.findout_is_gameover()

    def findout_is_gameover(self):
        """This method checks if all numbers in players's cards are guessed.
        """
        if not self.is_game_over:
            self.is_game_over = True if (self.my_card.number_guessed == 15
                                         or self.comp_card.number_guessed == 15) else False
        return self.is_game_over

    def print_endgame_message(self):
        """This method evaluates the message that should be printed according to who has won the game in a pretty way.
        It also prints statistic information about the game:
        - how many rounds were played,
        - what numbers were selected,
        - how many numbers have left,
        - what are these left numbers.
        """
        message = "Вы выиграли!" if self.my_card.number_guessed == 15 else "Компьютер выиграл!"
        print(message)
        end_message = f"Игра закончена!\n" \
                      f"В игре прошло {self.qt_rounds_played} раундов \n" \
                      f"Выпали числа: {self.numbers_played} \n" \
                      f"Осталось {len(self.numbers_left)} чисел \n" \
                      f"{self.numbers_left}"
        print(end_message)
