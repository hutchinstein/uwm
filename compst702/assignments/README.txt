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

dealer_action(player_score, dealer_score) is called during game_action if the player decides to stay.  It handles
the following:
1. It checks if the dealer score is less than or equal to the player score and less than 21
2. It checks if the dealer score is not equal to the player score
3. If both of these conditions are true it calls the hit() function, adding a card to the dealers hand.
4. display_status() is called to display both hands and the current score
5. This will loop as long as the first two conditions are true
6. After this loop is completed the game_action() process is resumed and game_result() is called

display_status() is called frequently throughout the program.  It handles the following:
1. It prints the dealer's and player's cards
2. It gets both scores and prints them

game_result() is called at the end of dealer_action().  It handles the following:
1. Uses update_player_purse by with result of scoring()
2. Sets playing variable to False

scoring() is called by game_result().  It handles the following:
1. Gets the player and dealer's scores
2. Follows a series of if-elif statements to determine the outcome
3. Returns either "victory" or "loss" which is used by update_player_purse()

update_player_purse() is called by game_result().  It handles the following:
1. Checks if blackjack variable has been set to True
2. If blackjack is True, the bet is set to bet * 1.5
3. Depending on the outcome of the game, the player is either awarded or deducted the bet
4. It prints out the current purse balance as well as win/loss record

add_to_purse() is called in two different areas within place_bet().  It handles the following:
1. Prompts the player to type in how much they would like to contribute
2. Updates the player purse total

hit(hand) is called in several areas.  It handles the following:
1. It takes the card at the top of the deck and adds it to the hand listed in the parameter

get_score(hand) is called in several areas.  It handles the following:
1. It splits the card into a value and suit
2. It uses the value portion against card_value dictionary to find value of the plain text
3. If the card is an 'Ace' special handling is required.  If the current score + 11 is greater than 21 then only 
1 is added to the score

write_to_file() is called by continue_check() once all player and dealer action is completed.  It handles
the following:
1. Checks if player is new or not
2. For new players it opens the players.txt file and appends the player information 
3. For returning players the players.txt file is opened and each name is checked to see if it matches the current 
player information.  If it does match, this information is overwritten by current player information.  All other 
cases the player information is added to a player_out string.  This player_out string is then written to the file.
4. Files are closed

continue_check() is called in main() after all player and dealer action is completed.  It handles the following:
1. Promts the player with an option to continue playing or not
2. If the player says 'y' main() is called
3. If the player says 'n' write_to_file() is called and and the game is overwrite
4. If the player enters an invalid selection continue_check() is called recursively 

main() is called after start_game and contains most of the game functions.  It handles the following:
1. Calls create_deck
2. Calls shuffle_deck
3. Calls place_bet
4. Calls deal()
5. Calls display_status
6. Initates game loop using a while loop
7. After games loop is completed, it calls continue_check()

##### How to run the program #####
This program can be run in the command line or in an IDE.  All files listed in 'programming task and its specifications' section
must be present or the program will crash.  Players.txt can be blank, however suits.txt and cards.txt cannot be altered.
All required player input will be displayed to the screen.

