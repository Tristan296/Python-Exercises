"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 
0 to n and return a new string.
"""

def rmFirstNChars(word, n):
    return word[n::]

print(rmFirstNChars("pynative", 4))
