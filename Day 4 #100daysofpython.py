#1. RANDOMISATION
# Creating a random decimal number between 0 and 5

import random

random_float = random.random()*5
print(random_float)


#2. HEADS OR TAILS
# Virtual coin toss program to give heads or tails

import random

random_int = random.randint(0, 1)

if random_int == 0:
    print("Heads!")
else:
    print("Tails!")


#3. BANKER ROULETTE (using split())
# USE OF LISTS
# Program that selects random names from a list of names. The selected person pays the bill.

import random

names = input("Give me the names of the people, separated by a comma. ")

names_list = names.split(",") # names converted to a list by separating out the commas using .split(",")

# getting the total number of items
items_number = len(names_list)

random_name = random.randint(0, items_number-1) # we need one less since our indexing starts from 0 and not 1 as the len()

selected_name = names_list[random_name]

print(f"{selected_name} will pay the bill!")


#4. choice() function
# Program that selects random names from a list of names. The selected person pays the bill.

import random

names = input("Give me the names of the people, separated by a comma. ")

names_list = names.split(",") # names converted to a list by separating out the commas using .split(",")

selected_name = random.choice(names_list) #randomly picks up a nam e from the list

print(f"{selected_name} will pay the bill!")
