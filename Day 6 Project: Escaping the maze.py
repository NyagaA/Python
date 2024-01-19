									# ESCAPING THE MAZE PROJECT
# Lost in a maze
# Write a program to help the Reeborg find the exit.
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while front_is_clear():
    move()
turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
