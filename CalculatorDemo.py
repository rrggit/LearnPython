def addition (a, b):
    res = a + b
    return res

def subtraction (a, b):
    res = a - b
    return res
    
def multiplication (a, b):
    res = a * b
    return res
    
def division (a, b):
    res = a / b
    return res

while True:
    print('1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n0) Exit')
    
    opt = int(input('Enter opt: '))
    if opt == 0:
        print('Bye Bye')
        break
    
    if opt > 4 or opt < 0:
        print('Enter correct option!')
        continue
    op1 = int(input('Enter operand 1: '))
    op2 = int(input('Enter operand 2: '))
    result = 0
    if opt == 1:
        result = addition(op1, op2)
    elif opt == 2:
        result = subtraction(op1, op2)
    elif opt == 3:
        result = multiplication(op1, op2)
    elif opt == 4:
        result = division(op1, op2)

    print('Result:', result)