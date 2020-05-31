print("class: SQUARE, CIRCLE, HEXAGON, TRIANGLE, PENTAGON, RECTANGLE, PARALLELOGRAM, TRAPEZIUM")

import turtle
import math


class SQUARE:
    def __init__(self):
        self.__side=150

    def get_side(self):
        return self.__side

    def get_area(self):
        return (self.__side**2)

    def get_perimeter(self):
        return (4*self.__side)

    def draw(self):
        #turtle.speed(1)
        turtle.color("blue")
        turtle.goto(self.__side,0)
        turtle.goto(self.__side,self.__side)
        turtle.goto(0,self.__side)
        turtle.goto(0,0)
c=SQUARE()
c.draw()
print("Area of circle is ", c.get_area())
print("Perimeter of circle is ", c.get_perimeter())
    

class CIRCLE():
    def __init__(self):
        self.__radius=100

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return (3.14*(self.__radius**2))

    def get_perimeter(self):
        return (2*3.14*self.__radius)

    def draw(self):
        #turtle.speed(1)
        turtle.color("red")
        turtle.circle(self.__radius)
c=CIRCLE()       
c.draw()
print("Area of circle is ", c.get_area())
print("Perimeter of circle is ", c.get_perimeter())


class HEXAGON():
    def __init__(self):
        self.__side=120

    def get_base(self):
        return self.__side

    def get_area(self):
        return (3*math.sqrt(3)*self.__side/2)
    
    def get_perimeter(self):
        return (6*self.__side)

    def draw(self):
        #turtle.speed(1)
        turtle.color("orange")
        #turtle.goto(0,self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
        turtle.right(60)
        turtle.forward(self.__side)
c=HEXAGON()
c.draw()
print("Area of hexagon is ", c.get_area())
print("Perimeter of hexagon is ", c.get_perimeter())


class TRIANGLE:
    def __init__(self):
        self.__base=250

    def get_base(self):
        return self.__base

    def get_height(self):
        return self.__height

    def get_area(self):
        return (math.sqrt(3)*self.__base**2/4)
    
    def get_perimeter(self):
        return (3*self.__base)

    def draw(self):
        #turtle.speed(1)
        turtle.color("green")
        #turtle.goto(self.__base, -0)
        turtle.right(120)
        turtle.forward(self.__base)
        turtle.right(120)
        turtle.forward(self.__base)
        turtle.right(120)
        turtle.forward(self.__base)
c=TRIANGLE()
c.draw()
print("Area of triangle is ", c.get_area())
print("Perimeter of triangle is ", c.get_perimeter())


class PENTAGON:
    def __init__(self):
        self.__side=150

    def get_base(self):
        return self.__side

    def get_area(self):
        return (0.84225*self.__side**2)
    
    def get_perimeter(self):
        return (5*self.__side)

    def draw(self):
        #turtle.speed(1)
        turtle.color("black")
        turtle.goto(self.__side,0)
        turtle.right(72)
        turtle.forward(self.__side)
        turtle.right(72)
        turtle.forward(self.__side)
        turtle.right(72)
        turtle.forward(self.__side)
        turtle.right(72)
        turtle.forward(self.__side)
c=PENTAGON()
c.draw()
print("Area of pentagon is ", c.get_area())
print("Perimeter of pentagon is ", c.get_perimeter())


class RECTANGLE:
    def __init__(self):
        self.__length=300
        self.__breadth=150

    def get_length(self):
        return self.__length
    def get_breadth(self):
        return self.__breadth

    def get_area(self):
        return (self.__length*self.__breadth)

    def get_perimeter(self):
        return (2*(self.__length + self.__breadth))

    def draw(self):
        #turtle.speed(1)
        turtle.color("#DC143C")
        turtle.right(72)
        turtle.forward(self.__length)
        turtle.right(90)
        turtle.forward(self.__breadth)
        turtle.right(90)
        turtle.forward(self.__length)
        turtle.right(90)
        turtle.forward(self.__breadth)
        turtle.right(90)
c=RECTANGLE()
c.draw()
print("Area of rectangle is ", c.get_area())
print("Perimeter of rectangle is ", c.get_perimeter())


class PARALLELOGRAM:
    def __init__(self):
        self.__length=300
        self.__breadth=150
        self.__height=100

    def get_length(self):
        return self.__length
    def get_breadth(self):
        return self.__breadth

    def get_area(self):
        return (self.__length*self.__height)

    def get_perimeter(self):
        return (2*(self.__length + self.__breadth))

    def draw(self):
        #turtle.speed(1)
        turtle.color("#191970")
        turtle.left(180)
        turtle.forward(self.__length)
        turtle.right(60)
        turtle.forward(self.__breadth)
        turtle.right(120)
        turtle.forward(self.__length)
        turtle.right(60)
        turtle.forward(self.__breadth)
        turtle.right(120)
c=PARALLELOGRAM()
c.draw()
print("Area of parallelogram is ", c.get_area())
print("Perimeter of parallelogram is ", c.get_perimeter())

    
class regtrapezium() :
    def __init__(self) :
        self.__eq_sides = 200
        self.__lside = 300
        
    def get_eq_sides(self) :
        return self.__eq_sides
    
    def get_lside(self) :
        return self.__lside
    
    def get_perimeter(self) :
        return (5*self.__eq_sides)
    
    def get_area(self) :
        return (3*self.__eq_sides*self.__eq_sides*1.7321)/4
    
    def draw(self) :
        turtle.color("#8B4513")
        turtle.forward(self.__lside)
        turtle.right(-120)
        turtle.forward(self.__eq_sides)
        turtle.right(-60)
        turtle.forward(self.__eq_sides)
        turtle.right(-60)
        turtle.forward(self.__eq_sides)
        turtle.right(-120)

c = regtrapezium()
c.draw()
print("Area of regular trapezium is ", c.get_area())
print("Perimeter of regular trapezium is ", c.get_perimeter())


