"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5
"""

def divByFive(lst):
    for num in lst:
        if (num % 5 == 0):
            print(num)
            
divByFive([10,20,33,46,55])