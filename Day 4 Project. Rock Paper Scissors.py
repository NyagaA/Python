                                                          # ROCK PAPER SCISSORS GAME
# Program that asks a user for a random choice between rock, paper and scissors, and compares it to the random computer's choice to determine the winner based on the Rock Paper Scissors Association rules.

import random

rock = '''
                    888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
'''

paper = '''
                                        
                                        
88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888          
'''

scissors = '''
                d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
'''
choice_img = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice in [0, 1, 2]:
    print(f"User choice: {user_choice}")
    print(choice_img[user_choice])

    comp_choice = random.randint(0, 2)
    print(f"Computer choice: {comp_choice}")
    print(choice_img[comp_choice])

    if user_choice == comp_choice:
        print("Outcome: Draw!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1) or (user_choice == 1 and comp_choice == 0):
        print("Outcome: You Win!")
    else:
        print("Outcome: You lose!")

else:
    print("You typed an invalid number, you lose!")
