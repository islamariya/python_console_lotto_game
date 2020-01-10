from lotto_cards import Card


class Dealer(object):
    """This class represents a computer player and stores information about:
    - player's name (str)
    - player's card and what numbers have been guessed so far
    - qt of guessed numbers.
    It has following methods:
    - checks if selected number is in players's card and marks it as guessed (ХХ);
    - prints player's card to console
    """

    def __init__(self):
        self.player_name = "Компьютер"
        self.player_card = Card().card_generation()
        self.number_guessed = 0
        self.is_last_selected_num_guessed = False

    def find_the_num_in_card(self, number):
        """ This method checks if selected number is in players's card, if necessary marks it as guessed (ХХ),
        increases qt of number_guessed and changes a flag is_last_selected_num_guessed. This flag helps to evaluate
        user's choice to mark as guessed.
        :param number: int
        :return: self.player_card (nested list), self.number_guessed (int), self.is_last_selected_num_guessed (bool)
        """
        self.is_last_selected_num_guessed = False
        for row in self.player_card:
            if number in row:
                row[row.index(number)] = "XX"
                self.number_guessed += 1
                self.is_last_selected_num_guessed = True
        return self.player_card, self.number_guessed, self.is_last_selected_num_guessed

    def print_a_card(self):
        """ This method prints players's card and the qt of guessed numbers in console in a pretty way
        """
        player_card = ""
        for i in self.player_card:
            new = list(map(lambda x: str(x), i))
            player_card += "\t".join(new)
            player_card += "\n"
        print(f"_______ Карточка {self.player_name} _______")
        print(f"Угадано {self.number_guessed} значений")
        print(player_card)


class Player(Dealer):
    """ This class represents a player and stores information about:
    - redefines player's name (str)
    - player's card and what numbers have been guessed so far
    - qt of guessed numbers.
    It has following methods:
    - checks if selected number is in players's card and marks it as guessed (ХХ);
    - ask player whether he wants to underline the selected number in card and evaluate the results.
    - checks if the user has won the game;
    - prints player's card to console
    """

    def __init__(self):
        Dealer.__init__(self)
        self.player_name = "Игрок 1"

    def underline_number(self, number, game):
        """This method ask user whether he wants to underline the selected number in card and evaluate the results.
        Blank input means NO, any symbol - Yes.
        The user lost the game if he decides to underline the number and it is not in card or the number is in, but
        user refuses to underline.
        :param number: int
        :param game: instance Raffle class
        :return: game.is_game_over: bool
        """
        self.decision = input("Зачеркнуть число в карточке? Нажмите любую клавишу или enter, чтобы не "
                              "зачеркивать\n").strip()
        self.find_the_num_in_card(number)
        if bool(self.decision) is True and bool(self.is_last_selected_num_guessed) is False or \
                bool(self.decision) is False and bool(self.is_last_selected_num_guessed) is True:
            game.is_game_over = True
            print("Вы проиграли!")
            return
        return game.is_game_over
