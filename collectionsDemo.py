# str

str1 = 'Codekul - The Gurukul for Coders!'
res = len(str1)

str2 = "Python Batch"
str3 = str1 + str2

str4 = str1.replace(" ", "_")
print(str4)

# List

list1 = [1,2,3,4,5,'Seven', 8.9, True]

list1.append(6)

list2 = [2,3,4]

list3 = list1 + list2
list3[2] = 30
list3.remove('Seven')
print(list3)

# dictionary

dict1 = {'key1': 'value1', 'key2': 'value2', 'abc': 123, 1: 'One'}
dict1['Two'] = 2
# print(dict1[2])

# tuple

t1 = (1,2,3,4, 'Five', 6.7, True)

print(t1[0])