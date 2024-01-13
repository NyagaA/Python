#1. IF_ELSE & COMPARISON OPERATORS

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride!")


#2. ODD OR EVEN EXERCISE
#Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#3. NESTED IF

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age =int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride!")


#4. IF/ELIF/ELSE

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age =int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride!")


#4. BMI CALCULATOR USING IF/ELIF/ELSE
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Enter your height in meters e.g., 1.55
height = float(input("What is your height in meters? "))
# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight in kilograms? "))

BMI = round(weight / height**2)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underwieght!")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight!")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight!")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese!")
else:
  print(f"Your BMI is {BMI}, you are clinically obese!")


#4. LEAP YEAR PROGRAM
# Write a program that checks if a year is a leap year or not

year = int(input("Which year do you want to check? "))\

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year!")
    else:
        print("Leap year!")
else:
    print("Not a leap year!")


#5. MULTIPLE IF STATEMENTS IN SUCCESSION
# ROLLERCOASTER RIDE

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age =int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Teen tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo? Y or N? ")
    if wants_photo == "Y":
        bill +=3
        
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride!")


#6. PIZZA ORDER

print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

if size == "S":
    bill += 15
    print("Small pizza is $15!")
elif size == "M":
    bill += 20
    print("Medium pizza is $20!")
else:
    bill += 25
    print("Large pizza is $25!")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size != "S":
        bill += 3
    
if extra_cheese == "Y":
    bill += 1    

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")


#7. LOVE SCORE CALCULATOR

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

names = name1.lower() + " " + name2.lower()

#TRUE COUNT
T = names.count("t")
R = names.count("r")
U = names.count("u")
E = names.count("e")

true_count = T + R + U + E

#LOVE COUNT
L = names.count("l")
O = names.count("o")
V = names.count("v")
E = names.count("e")

love_count = L + O + V + E

love_score_str = str(true_count) + str(love_count)
#love_score_str = int(str(true_count) + str(love_count))
love_score = int(love_score_str)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
