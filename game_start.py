from game_play_logic import Raffle


def main():
    """ This is a main function to launch the lotto game.
    There are 2 players in game: computer and user. Each player has 1 card with 15 unique numbers from 1 to 90.
    Each round Dealer selects a number. Player should confirm whether there is a selected number in his card.
    If he is mistaken, game automatically stops and he loses.
    Player who has guessed all 15 numbers win.
    """
    game = Raffle()
    while game.is_game_over is False:
        game.play_a_round()
    game.print_endgame_message()

if __name__ == "__main__":
    main()
