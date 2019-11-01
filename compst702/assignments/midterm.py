import random


def num_guess(game_number):
    game_counter = 0
    game_number = game_number
    game_over = False
    victory = False
    hidden_number = random.randint(1, 101)
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
    while playing:
        num_guess(game_number)
        continue_to_play = input("Press q to quit, press enter to continue ")
        if continue_to_play.lower() == "q":
            playing = False
        game_number += 1


main()
