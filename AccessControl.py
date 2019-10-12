class MyClass:
    def __init__(self, a):
        self.__a = a

    def __display(self):
        print ("a: ", self.__a)

    def setA(self, a):
        self.__a = a

    def info(self):
        self.__display()

obj = MyClass(10)
obj .__a = 20
obj .setA(30)
obj . info()