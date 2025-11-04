"""
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, 
the output shall be '6 3 5 7', with a space separating the digits.
"""

def reverseNum(n):
    return " ".join(str(n)[::-1]) # Convert number to string, reverse it and join with spaces

print(reverseNum(7536)) 
