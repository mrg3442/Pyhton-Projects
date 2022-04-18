from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


    def sqaureShape(self):
        print("A sqaure has 4 equal sides.") 

class Sqaure(Shape):
    def __init__(self, side):
        self.__side = side


    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side
    def volume(self):
        return 3 * self.__side
   

square = Sqaure(5)
print(square.area())
print(square.perimeter())
print(square.volume())
square.sqaureShape()
