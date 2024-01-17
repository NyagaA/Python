									                                        # PASSWORD GENERATOR PROJECT
  
#1. Easy Level - Order not randomised

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""

# nr_letters
for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    #print(random_letter)
    password += random_letter
    
# nr_symbols
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    #print(random_symbol)
    password += random_symbol
    
# nr_numbers
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    #print(random_number)
    password += random_number
    
print(password)



#2. Hard Level - Order of characters randomised

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []   # added as a list

# nr_letters
for value in range(1, nr_letters + 1):
    password += random.choice(letters)
    
# nr_symbols
for value in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    
# nr_numbers
for value in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    
print(password)

random.shuffle(password) # shuffles the order of characters in the password

strong_password = ""  # empty string
for value in password:
    strong_password += value
    
print(f"Strong password: {strong_password}")
