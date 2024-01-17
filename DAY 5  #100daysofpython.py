#1. AVERAGE HEIGHT

# Write a program that calculates the average student height from a List of heights
# Input a Python list of student heights
student_heights = input("What are the student heights in cm?\n").split(",")

# Converting the input student_heights from strings to integers
for n in range(0, len(student_heights)):        
    student_heights[n] = int(student_heights[n])  

# Converting the input student_heights from strings to integers using list comprehension:
#student_heights = [int(height) for height in student_heights]

# Total height
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height = {total_height}")

# Count of students
students_count = 0
for student in student_heights:
    students_count += 1
print(f"Number of students = {number_of_students}")

# Average height
avg_height = round(total_height / number_of_students)
print(f"Average height = {avg_height}")


#2. HIGHEST SCORE

# Write a program that calculates the highest score from a List of scores(Using for loop)
# Input a list of student scores
student_scores = input("Input a list of student scores.\n").split(",")

# Converting the input student_scores from strings to integers using list comprehension:
scores_list = [int(score) for score in student_scores]
                  
# Initialize the highest score variable with the first score in the list
highest_score = scores_list[0]

# Iterate through the list to find the highest score
for score in scores_list:
    if score > highest_score:
        highest_score = score
        
# Print the highest score
print(f"The highest score is: {highest_score}")


#3. ADDING EVEN NUMBERS

# Using the range() function
# Adding even numbers between 1 and 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)


# or
# total = 0
# for number in range(2, 101, 2):
    #total += number
# print(total)


#4. FIZZ BUZZ

# Write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
    # Your program should print each number from 1 to 100 in turn and include number 100.
    # When the number is divisible by 3, instead of printing the number, it should print "Fizz".
    # When the number is divisible by 5, instead of printing the number, it should print "Buzz".`
    # And if the number is divisible by both 3 and 5, print "FizzBuzz"


for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
