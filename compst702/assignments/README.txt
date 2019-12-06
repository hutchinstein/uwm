##### Programming task and its specifications #####
This program is a single player blackjack game.  In order for the game to run the following files need to be located
in the same directory:
1. players.txt
> This file can be empty, it will be read and populated as needed.  It stores player information.
2. cards.txt
> This file contains cards Ace through King and is used to create the deck
3. suits.txt
> This file contains all suits in the deck and is used to create the deck

##### Programming Design #####
start_game() is called first.  It handles the following:
1. Displays list of all saved players, allows user to select new or saved profile.
2. Creates new profile if needed.
3. Creates Player object

check_for_existing_user() is called within start_game() if a new user is to be created.  It handles the following:
1. Opens list of saved players.
2. Checks if the first and last name entered by the user matches any of the saved profiles.
3. Gives the user the option to overwrite an old profile or not.

create_deck() is first function called within main().  It handles the following:
1. Opens suits.txt & cards.txt, creates two lists from these files.
2. Uses a nested for loop to append suit names with card values and appends information to deck list.

shuffle_deck(my_deck) is called second within main().  It handles the following:
1. It reorders the deck that was created in create_deck() to simulate shuffling a deck of cards.

deal() is called third within main().  It handles the following:
1. It pops() a card to the players hand, then dealers hand.  It does this twice.

place_bet() is called fourth within main(). It handles the following:
1. It checks if the players purse is equal to zero, if it is, it calls add_to_purse() to add more money.
2. Prompts the user to enter a value to bet.
3. Checks if the user has enough money in their purse to pay for their bet, if not it calls add_to_purse() to add more.

game_action(player_score, dealer_score) is called fifth in main() and starts the active part of the game.  It handles
the following:
1. Checks the players score to determine if it is less than or equal to 21.
2. Allows players to hit (calling hit() function) or stay (calling dealer_action(player_score, dealer_score) function).
3. If the player score is greater than 21 it calls the game_result() function since the player has no other moves.
4. Checks if the player is still playing, if not game_result() is called to determine the outcome




##### How to run the program #####

