#1.  THE HURDLES 1 LOOP CHALLENGE
# Reeborg has entered a hurdles race, make him run the course.
# Number of hurdles is 6

#USING FOR LOOP

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for moves in range(6): # range(6) controls how many times we want to repeat the sequence of move() and jump() actions.
    move()
    jump()


#USING WHILE LOOP

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_hurdles = 6
while number_of_hurdles > 0:
    move()
    jump()
    number_of_hurdles -= 1


#2. THE HURDLES 2 LOOP CHALLENGE
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is.(number of hurdles not specified)
# Condition: at_goal() and its negation.

# Method 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    move()
    jump()

# or

#while not at_goal():
    #move()
    #jump()


#3. THE HURDLES 3 LOOP CHALLENGE
# The position and number of hurdles changes each time this world is reloaded.
# The conditions: front_is_clear() or wall_in_front() and at_goal().

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()


#4. THE HURDLES 4 LOOP CHALLENGE
# The position, the height and the number of hurdles changes each time the world is reloaded.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
