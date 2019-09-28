# Write a Python to count the occurrences of each character in string


str1 = "Codekul the place to learn coding"
char_freq = {} 
  
for i in str1: 
    if i in char_freq: 
        char_freq[i] += 1
    else: 
        char_freq[i] = 1

print ("Count of all characters in 'Codekul the place to learn coding' is :\n " +  str (char_freq))