def bin_dec(no):                                    #Declare a function bin_dec with value as "no" (a number)
    degree = 0                                      #Declare a variable degree set at 0
    decimal = 0                                     #Declare a variable decimal set at 0
    while no > 0:                                   #Condition (while) is that, number has to be greater than 0
        digit = no % 10                             #Variable digit is a number modulus of 10
        no = int (no / 10)                          #number is of type integer only, this will ignore values after decimal
        decimal = decimal + (digit * 2**degree)
        degree += 1
    return decimal


bin_no = int (input ("enter Binary no: " ))
dec_no = bin_dec (bin_no)
print ("decimal", dec_no)
