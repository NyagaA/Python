import random
from IPython.display import clear_output
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def number_range():
    """Return a random number between 0 and 100."""
    number = random.randint(0, 100)
    return number


def difficulty_level():
     while True:  # Keeps asking the user for input until a valid input is provided
        choose_difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
        if choose_difficulty_level == 'easy':
            return EASY_LEVEL
        elif choose_difficulty_level == 'hard':
            return HARD_LEVEL
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


def play_game():
    print("Welcome to the Number Guessing Game!")
    print(logo)
    
    
    number = number_range()    # Random number
    print("I'm thinking of a number between 0 and 100.")
    
    attempts = difficulty_level()   # Getting the number of attempts based on the chosen difficulty level
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}.")
            return    # Exiting the function if the guess is correct
        
        attempts -= 1

    print("You've run out of attempts. GAME OVER!")

    
game_over = False 
while not game_over:
    play_game_response = input("Do you want to play the Number Guessing Game? Type 'y' or 'n': ").lower()
    if play_game_response == "y":
        clear_output()
        # Run the game
        play_game()
    elif play_game_response == "n":
        game_over = True
        clear_output()
