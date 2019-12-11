import random

"""
Initialize variables
"""

# Global variables #
playing = True
ace = False
player_action = True
blackjack = False
new_player = True
greeting = True

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


"""
Player class and name functions
"""


class Player:
    """Player Class.  First name and last name are input by user for new players.
    All new players default wins, losses and purse is set to 0"""

    def __init__(self, f_name, l_name, wins, losses, purse):
        self.f_name = f_name
        self.l_name = l_name
        self.wins = wins
        self.losses = losses
        self.purse = purse


def get_fname():
    """Get player's first name"""
    fname = input("Enter your first name: ")
    fname = fname.strip()
    fname = fname.capitalize()
    return fname


def get_lname():
    """Get player's last name"""
    lname = input("Enter your last name: ")
    lname = lname.strip()
    lname = lname.capitalize()
    return lname


"""
Start in-game functions
"""


def start_game():
    """Start game is done before main loop to initialize the player.
    Players are able to save their name, wins, losses and purse, during
    this process they can choose to start with a saved character or
    start new."""
    global player, new_player, greeting
    new_player = True
    user_defined = False

    # Open list of players file #
    a = open("players.txt", "r")
    counter = 1
    print("Select your player:")

    # Generate list of players #
    for i in a:
        if i.strip().split(',')[0] == "":
            continue
        else:
            print(str(counter) + ".", i.strip().split(',')[0])
        counter += 1
    print(str(counter) + ". New Player")

    # Take in user selection #
    while not user_defined:
        try:
            player = int(input("Enter your selection: "))
            user_defined = True
        except ValueError:
            print("Invalid selection, please try again")
            # start_game()
        a.close()

    # Get player information #
    a = open("players.txt", "r")
    counter = 1
    for i in a:
        if i.strip().split(',')[0] == "":
            continue
        else:
            if counter == player:
                new_player = False
                fname = i.strip().split(',')[0]
                lname = i.strip().split(',')[1]
                wins = i.strip().split(',')[2]
                losses = i.strip().split(',')[3]
                purse = i.strip().split(',')[4]
        counter += 1
    a.close()

    # Create a new player #
    if new_player:
        player = Player(get_fname(), get_lname(), 0, 0, 0)
        check_for_existing_user()
        greeting = True
        if new_player:
            try:
                purse = int(input("New player created!\nHow much "
                                  "would you like to add to your purse $"))
            except ValueError:
                print("Please enter a number ")
            player.purse = purse

    else:
        player = Player(fname, lname, wins, losses, purse)
    if greeting:
        print("\nHello", player.f_name + ", welcome to Blackjack the Game. Good luck!\n")
        print("You have", player.purse, "in your purse.")


def check_for_existing_user():
    """Checks if first name and last name entered by user match name on the list
    User has the option to delete or try again"""
    global new_player, greeting
    a = open("players.txt", "r")
    for i in a:
        if i.split(',')[0].strip() == player.f_name.strip() and i.split(',')[1].strip() == player.l_name.strip():
            response = input("This player already exists, would you like to delete the old player? (y/n)")
            if response.lower() == "y":
                new_player = False
                continue
            elif response.lower() == 'n':
                greeting = False
                start_game()
            else:
                print("Invalid selection, please try again")
                check_for_existing_user()
    a.close()


def create_deck():
    """Each game starts with a new deck.  The card values and suits are stored in separate text files.
    A nested for loop generates all card combinations and appends to deck list"""
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
    """This function swaps a card at location i with a card at a random location between 0 & 51"""
    for i in range(0, len(my_deck)):
        rand_num = random.randint(0, 51)
        rand_card = deck[rand_num]
        temp_card = my_deck[i]
        my_deck[i] = rand_card
        my_deck[rand_num] = temp_card


def deal():
    """Deals cards one at a time to the player then dealer"""
    for i in range(0, 2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


def place_bet():
    """Takes in input from user to declare their bet.  If they do not have enough money in their purse
    they are prompted to try again."""
    if int(player.purse) == 0:
        print("You are out of money!  Please add more to continue.")
        add_to_purse(True)
    global bet
    try:
        bet = int(input("How much do you want to bet? "))
    except ValueError:
        print("Please enter an integer")
        place_bet()
    if bet > int(player.purse):
        response = input("You don't have enough in your purse! \nWould you like to add more? (y/n)")
        if response.lower() == 'y':
            add_to_purse()
        elif response.lower() == 'n':
            place_bet()
        else:
            print("Did not recognize your request")
            place_bet()
    else:
        return bet


def game_action(player_score, dealer_score):
    """After scores are displayed, players have the option to hit or stay.
    This handles player interaction.  Players are able to hit as long as they have 21 or fewer points."""
    global playing, player_action

    if player_score <= 21 and player_action:
        try:
            response = input("Would you like to (h)it or (s)tay? ")
            response = response.lower()
            if response == 'h':
                hit(player_hand)
            elif response == 's':
                dealer_action(player_score, dealer_score)
                playing = False
            else:
                print("\nPlease enter a valid response\n")
        except ValueError:
            print("\nPlease enter a valid response\n")
    elif player_score > 21:
        game_result()
    if dealer_score < 21 and not player_action:
        dealer_action(player_score, dealer_score)
    display_status()
    if not player_action:
        game_result()


def dealer_action(player_score, dealer_score):
    """After the player is done hitting the dealer is allowed to hit().
    This allows the dealer to hit() multiple times to get their score
    as close to 21 as possible."""
    global player_action
    player_action = False
    if 21 > get_score(dealer_hand) <= player_score and get_score(dealer_hand) != player_score:
        hit(dealer_hand)
    display_status()

    if get_score(dealer_hand) == player_score:
        display_status()
    elif 21 > get_score(dealer_hand) <= player_score:
        # dealer_action() is called recursively to allow for the dealer to hit multiple times #
        dealer_action(player_score, dealer_score)


def hit(hand):
    """Removes a card from the deck and adds it to the dealer or players hand"""
    hand.append(deck.pop())
    get_score(hand)


def get_score(hand):
    """Gets the value of the hand.
    If the value of a hand with an Ace in it will exceed 21 the value of the Ace is 1, otherwise it is 11
    """
    global ace
    ace = False
    score = 0
    for i in hand:
        card = i.split(" ")[0]
        if card == "Ace":
            ace = True
        value = card_value[card]
        score = score + value

    # Logic to handle aces.  10 is added to score if it will not cause the player to bust #
    if ace and score + 10 <= 21:
        score = score + 10
    return score


def display_status():
    """Uses get_score() function and displays current scores to the screen"""
    global playing
    if playing:
        print("Dealer's hand: ", dealer_hand, "\nPlayer's Hand: ", player_hand)
        dealer_score = get_score(dealer_hand)
        player_score = get_score(player_hand)
        print("Dealer's Score: ", dealer_score)
        print("Player's Score: ", player_score)


def game_result():
    """Calculates who wins the game and displays it to the screen."""
    global playing
    update_player_purse(scoring())
    playing = False


def scoring():
    """Scoring compares the player's and dealer's score and determines the winner.
    The goal is to get to 21 without going over.
    If the dealer and player tie, the dealer wins.
    If the player gets 21 and the dealer does not they earn 1.5 times the amount they bet.
    In all other cases the amount earned/lost is equal to the bet made"""
    result = ""
    global blackjack
    dealer_score = get_score(dealer_hand)
    player_score = get_score(player_hand)
    if player_score < 21 < dealer_score:
        print("You win!")
        result = "victory"
    elif player_score > 21:
        print("Busted!  You lose!")
        result = "loss"
    elif player_score > 21 < dealer_score:
        result = "victory"
        print("You win!")
    elif dealer_score == 21:
        print("Dealer has blackjack, you lose!")
        result = "loss"
    elif dealer_score == player_score:
        result = "loss"
        print("You lose!")
    elif dealer_score < 21 > player_score < dealer_score:
        result = "loss"
        print("You lose!")
    elif player_score == 21 and dealer_score > 21:
        print("Blackjack!  You win!")
        blackjack = True
        result = "victory"
    return result


def update_player_purse(result):
    """Called by game_result() to update the player's purse depending on the outcome of the game"""
    global bet, blackjack
    purse = int(player.purse)
    if blackjack:
        bet = bet * 1.5
    if result == "victory":
        purse += int(bet)
        player.wins = int(player.wins) + 1
    else:
        purse -= bet
        player.losses = int(player.losses) + 1
    player.purse = purse
    if int(purse) > 0:
        print("Your current purse is: ", int(player.purse))
    print("Current record:\n"
          "Wins:", player.wins, "Losses:", player.losses)
    blackjack = False


def add_to_purse(empty_purse=False):
    """Players can add to their purse if their bet is greater than their current purse
    or if their purse is empty.
    Parameter empty_purse is set to default to false.  This function can be checked during
    place_bet() and without this check the player is promoted twice to input their bet."""
    try:
        contribution = int(input("How much would you like to add to your purse? "))
        player.purse = str(int(player.purse) + int(contribution))
        if not empty_purse:
            place_bet()
    except ValueError:
        print("Please enter a valid number")
        add_to_purse()


def write_to_file():
    """This function writes player information to player text file.  If players already exist, their information
    will be overwritten.  Otherwise they are appended to the end of the file"""
    global new_player
    if new_player:
        file = open("players.txt", "a")
        out_string = "\n" + player.f_name + "," + player.l_name + "," + str(player.wins) + \
                     "," + str(player.losses) + "," + str(player.purse)
        file.write(out_string)
        file.close
    else:
        in_file = open("players.txt", "r")
        player_out = ""
        for i in in_file:
            if i.split(",")[0] == player.f_name:
                player_out = player_out + player.f_name + "," + player.l_name + "," + str(player.wins) + \
                     "," + str(player.losses) + "," + str(player.purse) + "\n"
            else:
                player_out = player_out + i
        in_file.close()
        out_file = open("players.txt", "w")
        out_file.write(player_out)


def continue_check():
    """After each game is completed, check if the player wants to continue.  If the do, they are returned
    to main.  Otherwise the player data is written to the player file."""
    # Global variables #
    global playing, player_hand, dealer_hand, player_action
    player_continue = input("\nWould you like to play another game? (y/n)")
    if player_continue.lower() == 'y':
        playing = True
        player_action = True
        player_hand, dealer_hand = [], []
        # Call to main() to play another game #
        main()
    elif player_continue.lower() == 'n':
        write_to_file()
        print("Goodbye,", player.f_name + ".")
    # Verify player response is valid #
    else:
        print("Invalid selection.")
        # Recursive call to validate player response #
        continue_check()


def main():
    """The main function of the program.  The player is initialized outside of this so they are not overwritten
    each time the function is called.
    First, the cards are dealt and initial scores are displayed.
    The game loop is then started by calling game_action().
    continue_check() is called to verify if the player wants to continue playing or not."""

    # Start first hand #
    create_deck()
    shuffle(deck)
    place_bet()
    deal()
    display_status()

    # Start game loop #
    while playing:
        game_action(get_score(player_hand), get_score(dealer_hand))
    continue_check()


start_game()
main()
