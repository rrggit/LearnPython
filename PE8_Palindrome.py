# Python program to check if a string is palindrome or not

# User inputs the string and it gets stored in variable x
x = input("Enter a string: ")
w = "" 
for i in x: 
	w = i + w 
	if (x==w): 
		print("YES")
else:
    print("No")