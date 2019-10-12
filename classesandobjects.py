class MyClass:

    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
        print('__init__')

    def display(self):
        print('Prop1: ',self.prop1)
        print('Prop2: ',self.prop2)


myObj = MyClass(1000, 2000)

myObj.display()

myObj.prop1 = 100
myObj.prop2 = 200

myObj.display()