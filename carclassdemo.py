class Car:
    def __init__(self, color, model, make):
        self.color = color
        self.model = model
        self.make = make
        self.speed = 0
        self.isEngineOn = False

    def info(self):
        print('Color:', self.color)
        print('Model:', self.model)
        print('Make:', self.make)
        print('Current Speed:', self.speed)
        print('Is Engine On:', self.isEngineOn)

    def start_engine(self):
        if self.isEngineOn:
            print('Engine is already started')
        else:
            self.isEngineOn = True

    def turn_off_engine(self):
        if self.isEngineOn == False:
            print('Engine is already turned off')
        else:
            self.isEngineOn = False

    def accelerate(self):
        if not self.isEngineOn:
            print('Engine is not started')
        else:
            self.speed += 1
    
    def apply_breaks(self):
        if self.speed == 0:
            print('Car is already stopped')
        else:
            self.speed -= 1

    def turn_right(self):
        print('{} colored {} is turning right'.format(self.color, self.model))

    def turn_left(self):
        print('{} colored {} is turning left'.format(self.color, self.model))
        

car1 = Car('Red', 'Alto', 'Suzuki')
car1.info()

car1.start_engine()
car1.accelerate()
car1.accelerate()

car1.apply_breaks()

car1.info()

car1.turn_left()
car1.turn_right()

car1.turn_off_engine()

car2 = Car('Black', 'i20', 'Hyundai')
car2.info()

car2.start_engine()
car2.accelerate()
car2.accelerate()
car2.accelerate()
car2.accelerate()

car2.apply_breaks()
car2.apply_breaks()

car2.turn_left()
car2.turn_right()

car2.info()

car2.turn_off_engine()