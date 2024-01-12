#1. TYPE CHECKING

num_char = len(input("What is your name?"))
    #print("Your name has " + num_char + "characters.")
print(type(num_char))


#2. TYPE CONVERSION/CASTING
num_char = len(input("What is your name?"))

new_num_char = str(num_char)  #converts num_char from int to str datatype

print("Your name has " + new_num_char + " characters.")


#3. Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Your program should work for different inputs. e.g. any two-digit number.
#The last line of your program should print the result.

two_digit_number = input("What is the two-digit number? ")

first_digit = int(two_digit_number [0])
second_digit = int(two_digit_number [1])

result = first_digit + second_digit
print(result)


#4. BMI CALCULATOR
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# convert the bmi to a whole number and print out a whole number

# 1st input: enter height in meters 
height = input("Enter height in meters: ")

# 2nd input: enter weight in kilograms
weight = input("Enter weight in kilograms: ")

#print(type(height))  #checking height datatype
#print(type(weight))  #checking weight datatype

weight_int = int(weight)  #converting from str to int datatype
height_int = float(height)  #converting from str to float datatype

# Using Exponent operator for calculation
BMI = weight_int / height_int**2

# Using Multiplication operator for calculation
BMI = weight_int / (height_int * height_int)

# Converting the bmi to a whole number
BMI_int = int(BMI)

print(BMI_int)


#4. FLOOR DIVISION

print(8 // 3)   #Results to an integer


#5. NUMBER MANIPULATION BASED ON PREVIOUS VALUE

score = 0
#If the score increases by 1
score +=1
print(score)


#6. Create a program using maths and f-Strings that tells us how many days, weeks and months we have left, if we live until 90 years old.

age = input("What is your age? ")

days = 365
weeks = 52
months = 12

#90 years calculation
days_90_yrs = 90 * days
weeks_90_yrs = 90 * weeks
months_90_yrs = 90 * months

#Current age calculation
days_age = int(age) * days
weeks_age = int(age) * weeks
months_age = int(age) * months

#Difference
days_left = days_90_yrs - days_age
weeks_left = weeks_90_yrs - weeks_age
months_left = months_90_yrs - months_age
years_left = 90 - int(age)

message = (f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
print(message)
