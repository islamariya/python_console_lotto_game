import random


class Card(object):
    """ Class Card creates a lotto game card for a player. Each card has 3 rows and 9 columns. There are 15
    numbers, for 5 in each row. There is only 1 number in each column in a row. Each column must
    have from 1 to 3 numbers. Numbers in each card in unique.
    Method card_generations implements generation of 15 unique numbers and puts them in a frame.
    Card example
        [[3,   15,   21, '_', 49, '_', 62,  '_',  '_'],
        ['_',  '_', '_', 36,  41, 58,  '_',  72,   82],
        [5,    '_', '_', 37,  46, '_', 64,   73,  '_']]
    """
    def card_generation(self):
        """This method generates a player's card. Card is nested list of 3 lists, each represents a rows.
        Each row contains 9 columns, each of them could contain numbers only of specific ten's (1-9, 10-19,
        20-29 ...80-90).
        There are 5 randomly chosen numbers in each row. There is only 1 number in each column in a row. In card as
        general, each column must have from 1 to 3 numbers. Numbers in each card in unique.
        Numbers generated consistently from 1st row to 3rd.
        First of all, for 1st row in a loop sys chooses number of column (0-9), adds it in list ("col_selected"),
        then randomly chooses a number related to this column and adds it to card. Column number and number do not
        take part in future selection for this row.
        For 2nd row sys takes remaining column numbers and add to it 1 randomly chosen from selected columns for 1st
        row. Selection process is the same.
        For 3rd row any of 0-9 column number can be chosen.
        :return: nested list of player card, see below for example
        [[3,   15,   21, '_', 49, '_', 62,  '_',  '_'],
        ['_',  '_', '_', 36,  41, 58,  '_',  72,   82],
        [5,    '_', '_', 37,  46, '_', 64,   73,  '_']]
        """
        self.player_card = [["_" for _ in range(9)] for _ in range(3)]
        possible_numbers_to_choose = [{j: "" for j in range(i, i + 10) if j > 0} for i in range(0, 90, 10)]
        possible_numbers_to_choose[8][90] = ""
        unused_col_numbers = list(range(9))
        col_selected_list = []
        row = 0
        while row < 3:
            for i in range(5):
                random.shuffle(unused_col_numbers)
                selected_col = unused_col_numbers.pop()
                col_selected_list.append(selected_col)
                number_selected = random.choice(list(possible_numbers_to_choose[selected_col].keys()))
                del possible_numbers_to_choose[selected_col][number_selected]
                self.player_card[row][selected_col] = number_selected
            row += 1
            unused_col_numbers.append(random.choice(col_selected_list))
            if row == 2:
                unused_col_numbers = list(range(9))
        return self.player_card

    def __init__(self):
        self.player_card = self.card_generation()
