#Functions for the devour all card game
#Python 3.6.5
#Windows 10


def instructions():
    """Instructions for the card game."""
    print(
        """
        Hello and welcome to the 'Devour All Card Game'.
        'Devour All' is a game played by a minimum of 2 to 5 players.
        The game consists of two rounds of playing.
        In the first round each player picks a random card
        from a deck and throws it on the table. If the card
        thrown on the table is the same suit as the card on top
        of the table, for example if they are both hearts, clubs,
        diamond or spades, the player is forced to devour all the
        cards on the table. The process will continue untill
        all the cards in the deck are finished. If any player
        does not have any cards in hand, then they will be
        declared as a winner.
        In the second round, if any players have cards in hand, then
        they will continue playing with the cards in their hands.
        Each player should pick a card from his/her hand and
        throw it on the table. If the card thrown on table
        is the same as the card on top of the table, then the
        player is forced to devour all the cards on the table.
        The game will continue until only one player is left
        with cards in hand. Then that player will be declared
        the loser. Hope you enjoy playing.
        """
        )
def create_players():
    pass

def comp_move():
    pass

def human_move():
    pass

instructions()
