def function_name():
    print('This is my function')

function_name()

def function_with_param(a, b):
    print('Value of a:', a)
    print('Value of b:', b)

function_with_param("ABC", 20)

def function_with_default(param1 = 10):
    print('Value of param1:', param1)

function_with_default(100)

def function_returning():
    return 'Codekul'

str1 = function_returning()
print(str1)