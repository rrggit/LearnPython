# Write a Python function to multiply all the numbers in a list

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((4, 5, 6, -7, 87)))