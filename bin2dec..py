def bin_dec(no):
    deg = 0
    dec = 0
    while no > 0:
        dig = no % 10
        no = int (no / 10)
        dec = dec + (dig * 2**deg)
        deg += 1
        return dec


bin_no = int (input ("enter Binary no: " ,))
dec_no = bin_dec (bin_no)
print ("decimal", dec_no)
