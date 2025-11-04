"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is a palindrome.
A palindrome number reads the same forwards and backward. 
For example, 545 is a palindrome number.
"""

def isPalindrome(num):
    num = str(num)
    return num[::-1] == num # checks if the str(num) reversed matches original.
    
print(isPalindrome(5333565))
print(isPalindrome(121))