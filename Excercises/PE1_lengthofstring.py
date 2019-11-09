# Count length of string & occurrence of each character in string

# User inputs the string and it gets stored in variable str
str1 = input("Enter a string: ")

# counter variable to count the character in a string
counter = 0
for s in str1:
      counter = counter+1
print("Length of the input string is:", counter)

char_freq = {} 
  
for i in str1: 
    if i in char_freq: 
        char_freq[i] += 1
    else: 
        char_freq[i] = 1

print ("Count of each character in given string is:\n " + str (char_freq))