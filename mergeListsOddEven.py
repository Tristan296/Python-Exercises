"""
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write Python code to create a new list 
containing odd numbers from the first list and even numbers 
from the second list.

Given:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

Expected Output:
result list: [25, 35, 40, 60, 90]
"""

def mergeLists(l1, l2):
    result_l = []
    for num in l1:
        if (num % 2 == 1):
            result_l.append(num)        
            
    for num in l2:
        if (num % 2 == 0):
            result_l.append(num)
            
    return result_l

print(mergeLists([10,20,25,30,35], [40,45,60,75,90]))
