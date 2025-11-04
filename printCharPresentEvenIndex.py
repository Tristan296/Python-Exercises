"""
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

"""

def printCharEvenIdx(s):
    for i, letter in enumerate(s): # Loop through the string with index
        if(i % 2 == 0): # Check if the index is even
            print(letter)
    
printCharEvenIdx("PYnative")