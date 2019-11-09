# Python program to print Even Numbers in a List 

# list of numbers 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# using list comprehension 
even_nos = [num for num in list1 if num % 2 == 0] 

print("Even numbers in the list: ", even_nos)