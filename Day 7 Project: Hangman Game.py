# SOLUTION 1

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Set 'lives' to equal 6.
lives = 6

# Print the game logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

# Main game loop
while "_" in display and lives > 0:
    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You have already guessed {guess}")
        continue  # Skip the rest of the loop and get a new input

    # Check guessed letter
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    # Print the hangman stage
    print(stages[lives])

# Check if the game ended because the user guessed all letters
if "_" not in display:
    print("Congratulations! You've guessed all the letters. You win!")
else:
    print("You are out of life, you lose!")
------------------------------------------------------------------------------------------------------------------------------------------------------------
# SOLUTION 2

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the game logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You have already guessed {guess}")
        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You are out of life, you lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You've guessed all the letters. You win!")

    # Print the hangman stage
    print(stages[lives])
