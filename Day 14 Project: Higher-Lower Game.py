# CODE 1
import random
from IPython.display import clear_output
from art import logo, vs
from game_data import data

def play_game():  # Defining the play_game function
    print("Welcome to the Higher-Lower Game!")  
    score = 0  # Initializing the score to zero
    against = random.choice(data)  # Selecting a random account to compete against
    
    while True:  
        
        print(logo)  

        # Randomly selecting two accounts to compare
        compare = against  # Assigning the current 'against' account to 'compare'
        print(f"Compare A:\n{compare['name']}, {compare['description']}, from {compare['country']}")  # Displaying details of 'compare'

        print(vs)  

        against = random.choice(data)  # Selecting a new random account for 'against'
        while against == compare:  # Ensuring 'against' is different from 'compare'
            against = random.choice(data)

        print(f"Against B:\n{against['name']}, {against['description']}, from {against['country']}")  # Displaying details of 'against'

        # Getting the followers count for each account
        compare_followers = compare['follower_count']
        against_followers = against['follower_count']

        # Player's choice
        user_choice = input("\nWho has more followers? Type 'A' or 'B' to choose: ").upper()

        # Validate user input
        while user_choice not in ['A', 'B']:  # Ensuring valid input
            print("Invalid input. Please choose 'A' or 'B'.")
            user_choice = input("Who has more followers? Type 'A' or 'B' to choose: ").upper()

        # Followers count comparison 
        if compare_followers > against_followers and user_choice == 'A':  
            clear_output()  
            score += 1  # Incrementing the score
            print(f"Correct! Your score is {score}")  
        elif compare_followers < against_followers and user_choice == 'B':  
            clear_output()  
            score += 1  
            print(f"Correct! Your score is {score}")  # Displaying correct guess message and current score
        else:
            clear_output()  
            print("Sorry, that's incorrect.")  
            print(f"Your score is {score}")  # Displaying final score
            break  # End the game if the guess is incorrect

# Start the game
play_game()  



# CODE 2
import random
from IPython.display import clear_output
from art import logo, vs
from game_data import data

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear_output()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()


# CODE 3
import random  
from IPython.display import clear_output  
from art import logo, vs  
from game_data import data  

def play_game():  # Defining the main game function
    score = 0  # Initializing the player's score

    while True:  # Starting an infinite loop for the game session
        print("Welcome to the Higher-Lower Game!")  # Displaying a welcome message
        print(logo)  # Displaying the game logo

        # Randomly selecting two accounts to compare
        compare = random.choice(data)  # First account
        print(f"Compare A:\n{compare['name']}, {compare['description']}, {compare['country']}")  # Displaying first account details

        print(vs)  # Displaying the versus logo

        against = random.choice(data)  # Second account
        while against == compare:  # Ensuring the second account is different from the first
            against = random.choice(data)

        print(f"Against B:\n{against['name']}, {against['description']}, {against['country']}")  # Displaying the second account details

        # Getting the followers count for each account
        compare_followers = compare['follower_count']
        against_followers = against['follower_count']

        # Asking the player's choice
        user_choice = input("\nWho has more followers? Type 'A' or 'B' to choose: ").upper()

        # Validating user input
        while user_choice not in ['A', 'B']:  # Ensuring the input is either 'A' or 'B'
            print("Invalid input. Please choose 'A' or 'B'.")
            user_choice = input("Who has more followers? Type 'A' or 'B' to choose: ").upper()

        # Comparing the followers count and updating the score accordingly
        if compare_followers > against_followers and user_choice == 'A':
            print(f"Correct! {compare['name']} has more followers.")
            score += 1
            print(f"Your score is {score}")
        elif compare_followers < against_followers and user_choice == 'B':
            print(f"Correct! {against['name']} has more followers.")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Sorry, that's incorrect.")
            print(f"Your score is {score}")

        # Asking if the user wants to play again
        while True:  # Starting an inner loop to handle play again input
            play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again == 'n':  
                clear_output()  
                print("Thanks for playing!")  
                print(f"Your score is {score}")  
                return  # Exiting the function to end the game
            elif play_again == 'y':  
                clear_output()  
                break  # Exiting the inner loop to continue playing
            else:
                print("Invalid input. Please type 'y' or 'n'.")  # Prompting for valid input

# Starting the game
game_over = False  # Initializing the game over flag
while not game_over:  
    play_game_response = input("Do you want to start the Higher-Lower Game? Type 'yes' or 'no': ").lower()
    if play_game_response == "yes":  
        clear_output()  # Clearing the output
        # Running the game
        play_game()
    elif play_game_response == "no":  
        game_over = True  # Setting the game over flag to end the loop
