# Intro to Python Async Work
# Monday March 11th, 2024.

# INSTRUCTIONS
# Create a new python file called async_3_11.py
# Answer the following questions. Once you've completed the questions, commit
# and sync your work.
# This activity must be completed by the end of class in order to recieve
# a grade.

# REMEMBER - TAKE YOUR TIME AND DO YOUR BEST! DO NOT GIVE UP! 

# 1. Which Python datacasting function would
# you use if you wanted to convert a string data type
# into an integer data type? Please write your response
# in a complete sentence. 
ro convert a string data type into an integer data type in phyton you would use the int() function
# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.
numbCol =[red,blue,green ,5,10,15] 
# 3. You have been hired by a University to create
# a scholarship function. The client would like to provide 
# students a scholarship to their school based on the following
# conditions; 
# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.
# The client would like you to use the logical NOT operator that will
# compare the condtions and return false. If the result is false, the client
# would also like the program to print the message "congrats! you've gotten the scholarship."
# the client has given you the choice on how to enter data for your function.
# you may enter data using input or pass in data into your function as parameters. 
def calculate_scholarship(gpa):
    if gpa >= 3.5 and gpa <= 4.0:
        return 5000
    elif gpa >=3.0 and gpa <3.5:
        return 3000
    elif gpa >=2.5 and gpa <3.0:
        return 1000
    else:
        return 0 