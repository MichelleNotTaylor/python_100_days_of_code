from random import randint

play = True

while play:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_of_guesses = 6

    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(game_mode == 'easy'):
        number_of_guesses = 10
    

    print(number_of_guesses)
    
    print(game_mode)

    guessing = True
    number_to_guess = randint(1, 100)

    while(guessing):
        user_guess = input("Make a guess: ")
        if(int(user_guess) < number_to_guess and number_of_guesses != 0):
            number_of_guesses -= 1
            print("Too low, guess again.")
        elif(int(user_guess) > number_to_guess and number_of_guesses != 0):
            number_of_guesses -= 1
            print("Too high, guess again.")
        else:
            print("You win!")
            guessing = False

        if(number_of_guesses == 0):
            print("You have run out of guesses. You lose!")
            guessing = False

        print("Number of guesses: " + str(number_of_guesses))

    continue_playing = input("Would you like to play again? y/n: ")
    if(continue_playing == 'n'):
        play = False
