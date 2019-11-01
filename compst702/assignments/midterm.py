# This program picks a random number between 1 and 100 the user then   #
# has 8 attempts to guess the number. For each guess the user is told  #
# if their guess was too high or too low.  All guesses are printed     #
# to the screen as well as the number of guesses remaining.  If the    #
# user guesses the answer correctly the game ends.  A second function  #
# is called once the game is over to write to a file the game number   #
# currently being played and the result; victory or loss.  After each  #
# game the user can choose to continue playing or quit.  To track each #
# session of game play when a new series of games is started the       #
# program writes to the score file the start time and end point of     #
# the session.                                                         #

import random
from datetime import datetime


def num_guess(game_number):
    game_counter = 0
    game_number = game_number
    game_over = False
    victory = False
    hidden_number = random.randint(1, 100)
    total_games = 8
    guessed_numbers = []
    while not game_over:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess > hidden_number:
            guessed_numbers.append(user_guess)
            print("Your guess is too high, try again!  You have " + str(total_games - (game_counter + 1)) +
                  " guesses remaining")
            print("You have guessed: ", guessed_numbers)
        elif user_guess < hidden_number:
            guessed_numbers.append(user_guess)
            print("Your guess is too low, try again!  You have " + str(total_games - (game_counter + 1)) +
                  " guesses remaining")
            print("You have guessed: ", guessed_numbers)
        else:
            print("Good job, you guessed the number!")
            game_over = True
            victory = True
        game_counter += 1
        if game_counter > total_games - 1:
            game_over = True
    if game_over and victory:
        outcome = "Victory"
    else:
        outcome = "Loss"
        print("The secret number was", hidden_number)
    score_keeping(outcome, game_number)


def score_keeping(outcome, games_played):
    file = open("output.txt", "a+")
    output_string = "Game " + str(games_played) + " ended in a " + outcome.lower() + "\n"
    print(output_string)
    file.write(output_string)
    file.close()


def main():
    playing = True
    game_number = 1
    file = open("output.txt", "a+")
    start_time = str(datetime.now())
    start_time = start_time[:-7]
    start_string = "\nNow tracking games started at " + start_time + "\n"
    file.write(start_string)
    file.close()
    while playing:
        num_guess(game_number)
        continue_to_play = input("Press q to quit, press enter to continue ")
        if continue_to_play.lower() == "q":
            playing = False
            file = open("output.txt", "a+")
            quit_string = "Games started at " + start_time + " over. \n"
            file.write(quit_string)
            file.close()
        game_number += 1


main()
