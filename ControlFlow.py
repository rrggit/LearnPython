'''
    if condition:
        true statements
    else:
        false statements
    if condition:
        statements
    elif condition:
        statements
    else:
        statements
'''
a = 20
b = 20

if a < b:
    print('a is less than b')
else:
    print('a is greater than b')
    print('This is inside else')
print('This is outside else')


if a < b:
    print('a is less than b')
    if a == 10:
        print('a is equal to 10')
elif a == b:
    print('a and b are equal')
    if b == 20:
        print('b is equal to 20')
else:
    print('a is greater than b')

# Loops


'''
while condition:
    statements
    incr/decr
'''
# i = 0
# while i < 10:
#     print('Codekul')
#     i += 1

# Sum of all even elements from 0-20

i = 0
even_sum = 0
odd_sum = 0

while i <= 20:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

'''
for item in collection:
    statements
'''

# for ch in "Codekul":
#     if ch == "C":
#         print(ch)

l1 = [23,4,78,23,78,35,83]
# sum = 0
for no in l1:
    if no % 2 == 0:
        print('{} is even'.format(no))
    else:
        print('{} is odd'.format(no))

# print('Sum:', sum)