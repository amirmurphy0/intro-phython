# Async Assignment March 3rd, 2024. 

# Complete and solve the following prompts.
# Make sure to write down the clues and keywords you found.
# (Make sure to include your clues and keywords to recieve full credit)

# Commit and sync your work before the end of class. 
# This will count toward your class activity grade. 

# Prompt #1- Elevator Conditional Function Execercise.

# You have been hired by a architeture firm to assist 
# with developing their elevator system. They have asked 
# you to develop a function that will accept a user's input. 
# your program should ask the user to enter a floor number. 
# When an user enters a number they will be sent to a specific 
# floor in the building. If the user enters a floor number that does not
# exist, your program should inform the user that the floor they entered
# does not exist and to enter another number and to try agin.

# The architects have given you the following 
# lists of floors for their building:

M = 'lobby'
B = 'basement'
R = 'rooftop'
_1 = 'gym'
_2 = 'restuarant'
_3 = 'workspace'
_4 = 'living quarters'

def ElevatorSystem():
    floors = input('what floor would u like to go too ')
    if floors==M:
        print('you are going to the lobby')

    elif floors ==B:
        print("your going to the basement")
    elif floors ==R:
        print("your going to the rooftop")
    elif floors ==_1:
        print("your going to the gym")
    elif floors ==_2:
        print("your going to the resturant")
    elif floors ==_3:
        print("your going to the workspace")
    elif floors ==_4:
        print("your going to the living quaters")
    else:
        print('your floor does not exist')
ElevatorSystem()

#___________________________________________________________

# Prompt #2- Amusement Park Conditional Function
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 