#Prompt for input from user
num = int (input ("Enter a number greater than 1: "))

# A prime number is greater than 1
if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print (num, "is not a prime number")
            break
    else:
        print (num, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(num, "is not a prime number")