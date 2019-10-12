#  Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
#  The element value in the i-th row and j-th column of the array should be i*j.

n = int (input("Input number of rows: "))
m = int (input("Input number of columns: "))

l1 = []
i = 0
while i < n:
    j = 0
    l2 = []
    while j < m:
        l2.append(i*j)
        j += 1

    l1.append(l2)
    i += 1

print(l1)