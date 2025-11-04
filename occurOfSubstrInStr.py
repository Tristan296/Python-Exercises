"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears
in the given string.
"""

def numOccurOfSubstr():
    str_x = "Emma is a good developer. Emma is a writer."
    str_to_find = "Emma"
    
    substr_frequency = str_x.count(str_to_find) # counts occurrences of str_to_find in str_x
    print(f"{str_to_find} appeared {substr_frequency} times") 
    
numOccurOfSubstr()