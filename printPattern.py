"""
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

# NOTE: the Solution given used a nested for loop, which is not necessary
# as we can simply multiple the string conversion of each number 
# by the value of the string. E.g. print("3" * 3) -> 333

def printTreePattern():
    for i in range(1, 6):
        str_num = str(i)
        print((str_num + " ") * i)
        
printTreePattern()
    