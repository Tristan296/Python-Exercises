# Write Python code to iterate through the first 10 numbers and, 
# in each iteration, print the sum of the current and previous number.

def print_sum():
    my_list = list(range(10)) # Creates a list of numbers from 0 to 9
    for index, value in enumerate(my_list):
        result = 0
        if index == 0: # No previous number for the first element
            previous_index = None
        else:
            previous_index = index - 1 # Get the previous index
            result = value + previous_index
        print(f"Current Number: {value} Previous Number: {previous_index}  Sum: {result}")
        
print_sum()