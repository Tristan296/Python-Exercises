"""
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s
first and last numbers are the same. 
If the numbers are different, return False.
"""

def firstLastSame(numList):
    return numList[0] == numList[len(numList)-1] # Compare first and last elements of the list

print(firstLastSame([10,20,30,40,10]))
print(firstLastSame([75,30]))
print(firstLastSame([1]))