"""
Using the classes in Example 2, include a Triangle class that extends GeometricObject.
The class contains:
  • Three float data fields named side1, side2, and side3 to denote the three sides of the triangle.
  • A constructor that creates a triangle with the specified side1, side2, and side3 with default values of 1.0.
  • The accessor and mutator methods for all three data fields.
  • A method named getArea() that returns the area of the triangle.
  • A method named getPerimeter() that returns the perimeter of the triangle.
  • A method named __str__() that returns a string description of the triangle which shows its three sides.

Produce the output for the triangle object similar to Example 3.
"""

import math

class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

# Triangle class
class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = float(side1)
        self.__side2 = float(side2)
        self.__side3 = float(side3)

    # Accessors
    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    # Mutators
    def setSide1(self, side1):
        self.__side1 = float(side1)

    def setSide2(self, side2):
        self.__side2 = float(side2)

    def setSide3(self, side3):
        self.__side3 = float(side3)

    # Calculations
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2.0
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return super().__str__() + " side1: " + str(self.__side1) + " side2: " + str(self.__side2) + " side3: " + str(self.__side3)

# Displaying function
def displayObject(g):
    print(g.__str__())

def main():
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    color = input("Enter color: ")
    filled_input = input("Is filled? (t/f or true/false): ").strip().lower()
    filled = filled_input in ["t", "true"]

    triangle = Triangle(side1, side2, side3)
    triangle.setColor(color)
    triangle.setFilled(filled)

    print("\n---Outputs---")
    print(f"""
Area: {triangle.getArea()}
Perimeter: {triangle.getPerimeter()}
Color: {triangle.getColor()}
Is filled? {triangle.isFilled()}
    """)

if __name__ == "__main__":
    main()