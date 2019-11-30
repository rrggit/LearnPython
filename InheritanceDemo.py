class A:

    def __init__(self):
        self.a = 10

    def info(self):
        print('a:', self.a)


class B(A):

    def __init__(self):
        self.b = 20
        A.__init__(self)

    def info(self):
        A.info(self)
        print('b:', self.b)

objB = B()
objB.info()
objB.b = 200
objB.info()

objB.info()
objB.a = 100
objB.info()