'''
In this final project, you will come up with a programming task for which you will write your own program.
It should be a purposeful and non-trivial program, bigger than any programming assignment. But it should
not be something too ambitious that you may not end up finishing by the deadline. The program must not be
something available on the Internet or in a book. The program must satisfy the following five requirements:

It must define and appropriately use at least one class.
It must use at least two meaningful functions besides main function and the class methods.
Its input and output must be through files (some user input, or output to screen is ok in addition, if needed)
It must use at least one list or one dictionary.
The program must be well documented with module documentation (three double-quote comments) for functions and
classes as well as comments at appropriate places in the program.
'''

'''
My Ideas
Create a GUI dictionary
Blackjack
    - Decks to play with are a class, can select how many decks will be shuffled
    - Generate cards using a dictionary
    - Create a user profile
        - Users are a class
        - User info can be loaded from a dictionary given by the user or a new one can be generated
'''


class Player:
    def __init__(self, f_name, l_name, wins, losses):
        self.f_name = f_name
        self.l_name = l_name
        self.wins = wins
        self.losses = losses


class Deck:
    def __index__(self, decks):
        # decks = the number of decks used in the current game
        self.decks = decks



