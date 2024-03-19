# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.

 def count_characters(string):
 return len(string)
# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 
#this code will let the user to enter a string then call the count_characters() function with the users input as the argument 
#the function will return the number of characters in the users input 

# 2. Use your notes, W3schools, and what we have learned in class to develop
# a simple rock, paper, scissors game. Your game should allow the user to enter a letter
# that will represent the values rock, paper, and scissors (ex. r = rock, p = paper, s= scissors). 
 def winner(Computer_Move,Player_Move):
    if Computer_Move == Player_Move:
        print('Tie')
    elif Player_Move == 'Rock' and Computer_Move == 'paper':
        winner = 'computer'
    elif Player_Move == 'paper' and Computer_Move == 'Scissor':
        winner = 'Computer'
    elif Player_Move == 'Scissor' and Computer_Move == 'Rock':
        winner = 'Computer'
    elif Player_Move == 'paper' and Computer_Move == 'Rock':
        winner = 'Player'
    else:
        print('Computer Win.')
winner('paper','Rock')
# EXTREMELY IMPORTANT NOTE
# at the top of you page write import random
# use the random.randrange(1,3) function to develop your random value logic 
# for your rock, paper, scissor game. 

# Please describe the steps you took, or if you weren't able to complete this activity,
# the steps you would've taken to solve this problem in complete sentences. 
# This must be completed in order to get full credit.  