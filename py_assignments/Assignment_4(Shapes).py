print("classes: square, circle, rectangle, parallelogram, hexagon, pentagon")


import turtle
import math

height=150          #global variable

print("1) Square")
class square():
    def __init__(self):
        self._side=200

    def get_side(self):
        return self.__side

    def get_perimeter(self):
        return 4*self._side

    def get_area(self):
        return self._side**2

    def draw(self):
        turtle.color("blue")
        turtle.goto(self._side, 0)
        turtle.goto(self._side, self._side)
        turtle.goto(0,self._side)
        turtle.goto(0, 0)

c=square()
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())

print("2) Circle")
class circle(square):
    def get_side(self):
        return self._side

    def set_side(self, s):
       self._side=s 

    def get_perimeter(self):
        return 2*3.14*self._side

    def get_area(self):
        return 3.14*self._side**2

    def draw(self):
        turtle.color("red")
        turtle.circle(self._side)

c=circle()
c.set_side(100)
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())

print("3) Triangle")
class triangle(square):    
    def get_side(self):
        return self._side

    def get_area(self):
        return (math.sqrt(3)*self._side**2/4)
    
    def get_perimeter(self):
        return (3*self._side)

    def draw(self):
        turtle.color("green")
        turtle.right(180)
        turtle.right(120)
        turtle.forward(self._side)
        turtle.right(120)
        turtle.forward(self._side)
        turtle.right(120)
        turtle.forward(self._side)
c=triangle()
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())



print("4) rectangle")
class rectangle():
    def __init__(self):
        self._length=300
        self._breadth=150

    def get_length(self):
        return self._length
    def get_breadth(self):
        return self._breadth

    def get_area(self):
        return (self._length*self._breadth)

    def get_perimeter(self):
        return (2*(self._length + self._breadth))

    def draw(self):
        #turtle.speed(1)
        turtle.color("#DC143C")
        #turtle.right(72)
        turtle.forward(self._length)
        turtle.left(90)
        turtle.forward(self._breadth)
        turtle.left(90)
        turtle.forward(self._length)
        turtle.left(90)
        turtle.forward(self._breadth)
        turtle.left(90)
c=rectangle()
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())

print("5) parallelogram")
class parallelogram(rectangle):
    def get_length(self):
        return self._length
    
    def get_breadth(self):
        return self._breadth

    def get_area(self):
        return (self._length*height)

    def get_perimeter(self):
        return (2*(self._length + self._breadth))

    def draw(self):
        #turtle.speed(1)
        turtle.color("#191970")
        turtle.left(180)
        turtle.forward(self._length)
        turtle.right(60)
        turtle.forward(self._breadth)
        turtle.right(120)
        turtle.forward(self._length)
        turtle.right(60)
        turtle.forward(self._breadth)
        turtle.right(120)
c=parallelogram()
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())


print("6) Hexagon")
class hexagon(square):
    def get_side(self):
        return self._side

    def set_side(self, s):
        self._side=s

    def get_area(self):
        return (3*math.sqrt(3)*self._side/2)
    
    def get_perimeter(self):
        return (6*self._side)

    def draw(self):
        #turtle.speed(1)
        turtle.color("orange")
        #turtle.goto(0,self.__side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
c=hexagon()
c.set_side(150)
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())

print("7) Pentagon")
class pentagon:
    def get_side(self):
        return self._side

    def set_side(self, s):
        self._side=s

    def get_area(self):
        return (0.84225*self._side**2)
    
    def get_perimeter(self):
        return (5*self._side)

    def draw(self):
        #turtle.speed(1)
        turtle.color("black")
        turtle.goto(self._side,0)
        turtle.right(72)
        turtle.forward(self._side)
        turtle.right(72)
        turtle.forward(self._side)
        turtle.right(72)
        turtle.forward(self._side)
        turtle.right(72)
        turtle.forward(self._side)
c=pentagon()
c.set_side(160)
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())


print("8)Rhombus ")
class rhombus(square):
    def get_side(self):
        return self._length

    def get_area(self):
        return (self._length*height)

    def get_perimeter(self):
        return (4*(self._side))

    def draw(self):
        turtle.goto(0, self._side)
        turtle.color("#8B4513")
        turtle.left(180)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(120)
        turtle.forward(self._side)
        turtle.right(60)
        turtle.forward(self._side)
        turtle.right(120)
c=rhombus()
c.draw()
print("perimeter: ", c.get_perimeter())
print("area: ", c.get_area())



