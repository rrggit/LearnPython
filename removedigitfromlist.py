# Write a function to remove numbers from the given list
# Given list is (13, 'ABC', 'True', 45, 34, 'Red', 'Green', 'Five', 5, 'Six')
# Expected output is ('ABC', 'True', 'Red', 'Green', 'Five', 'Six')

def remove_numbers_from_list(l):

    i = 0                                                   # Counter set to 0                                  
    length = len(l)                                         #
                                                    
    while i < length:                                   
        if isinstance (l[i], int):                           
            l.remove(l[i])
            length -= 1
        
        else:
            i += 1

    return l

list1 = (13, 'ABC', 'True', 45, 34, 'Red', 'Green', 'Five', 5, 'Six')
list2 = remove_numbers_from_list (list1)
    
print (list1)
print (list2)