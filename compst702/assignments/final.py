import random
'''
In this final project, you will come up with a programming task for which you will write your own program.
It should be a purposeful and non-trivial program, bigger than any programming assignment. But it should
not be something too ambitious that you may not end up finishing by the deadline. The program must not be
something available on the Internet or in a book. The program must satisfy the following five requirements:

It must define and appropriately use at least one class. - Done
It must use at least two meaningful functions besides main function and the class methods. - Done
Its input and output must be through files (some user input, or output to screen is ok in addition, if needed) 
It must use at least one list or one dictionary.
The program must be well documented with module documentation (three double-quote comments) for functions and
classes as well as comments at appropriate places in the program.
'''

'''

Things to do:
1. In game betting
2. Pay out after each game
3. Allow player to add more money to their purse if they run out
4. Write to some out file
5. Documentation: "module documentation (three double-quote comments) for functions and
classes as well as comments at appropriate places in the program."

Nice to have:
1. Save list of players and their attributes to a text file
    a. allow new players to add themselves to the list
2. GUI?

'''

# Global variables #
playing = True
ace = False
player_action = True
player = ""
suits = []
cards = []
deck = []
player_hand = []
dealer_hand = []

# Dictionary to convert card name to value #
card_value = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 1
}


# Player definition #
class Player:
    def __init__(self, f_name, l_name, wins, losses, purse):
        self.f_name = f_name
        self.l_name = l_name
        self.wins = wins
        self.losses = losses
        self.purse = purse


# Get player name
def get_fname():
    fname = input("Enter your first name: ")
    fname = fname.strip()
    fname = fname.capitalize()
    return fname


def get_lname():
    lname = input("Enter your last name: ")
    lname = lname.strip()
    lname = lname.capitalize()
    return lname


# Game functions #


# Start game is done before main loop to initialize the player
def start_game():
    global player
    player = Player(get_fname(), get_lname(), 0, 0, 0)
    print("Hello", player.f_name + ", welcome to Blackjack the Game. Good luck!")
    create_deck()
    shuffle(deck)
    try:
        purse = int(input("How much would you like to add to your purse $"))
    except ValueError:
        print("Please enter a number ")
    player.purse = purse


def create_deck():
    suit_list = open("suits.txt", "r")
    card_list = open("cards.txt", "r")
    for i in suit_list:
        i = i.strip("\n")
        suits.append(i)
    for i in card_list:
        i = i.strip("\r\n")
        cards.append(i)
    suit_list.close()
    card_list.close()
    for suit in suits:
        for card in cards:
            new_card = card + " of " + suit
            deck.append(new_card)


def shuffle(my_deck):
    for i in range(0, len(my_deck)):
        rand_num = random.randint(0, 51)
        rand_card = deck[rand_num]
        temp_card = my_deck[i]
        my_deck[i] = rand_card
        my_deck[rand_num] = temp_card


def deal():
    for i in range(0, 2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


def hit(hand):
    hand.append(deck.pop())
    get_score(hand)


def get_score(hand):
    ace = False
    score = 0
    for i in hand:
        card = i.split(" ")[0]
        if card == "Ace":
            ace = True
        value = card_value[card]
        score = score + value
    if ace and score + 10 <= 21:
        score = score + 10
    return score


def display_status():
    global playing
    if playing:
        print("Dealer's hand: ", dealer_hand, "\nPlayer's Hand: ", player_hand)
        dealer_score = get_score(dealer_hand)
        player_score = get_score(player_hand)
        print("Dealer's Score: ", dealer_score)
        print("Player's Score: ", player_score)


def game_action(player_score, dealer_score):
    global playing, player_action
    # hitting = True
    if player_score <= 21 and player_action:
        try:
            response = input("Would you like to (h)it or (s)tay? ")
            response = response.lower()
            if response == 'h':
                hit(player_hand)
            elif response == 's':
                dealer_action(player_score, dealer_score)
                # hitting = False
                playing = False
        except ValueError:
            print("Please enter a valid response")
    elif player_score > 21:
        print("Busted!")
        playing = False
    if dealer_score < 21 and not player_action:
        dealer_action(player_score, dealer_score)

    display_status()
    if not player_action:
        game_result(player_score, dealer_score)


def game_result(player_score, dealer_score):
    global playing
    print(player_score, dealer_score, "Game result")
    playing = False


def dealer_action(player_score, dealer_score):
    global player_action
    player_action = False
    if 21 > dealer_score <= player_score:
        hit(dealer_hand)

    display_status()
    if 21 > get_score(dealer_hand) <= player_score:
        dealer_action(player_score, dealer_score)


def main():
    # Initialize game #
    global playing, player_hand, dealer_hand, player_action

    # Start first hand #
    deal()
    display_status()

    # Start game loop #
    while playing:
        game_action(get_score(player_hand), get_score(dealer_hand))

    player_continue = input("Would you like to play another game? (y/n) ")
    if player_continue == 'y':
        playing = True
        player_action = True
        player_hand, dealer_hand = [], []
        main()
    else:
        print("Goodbye,", player.f_name)


start_game()
main()
