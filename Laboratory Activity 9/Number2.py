"""
Using your outputs from the Triangle class from the previous example, define a custom
exception class named TriangleError that extends RuntimeError. The TriangleError class
contains three private data fields: side1, side2, and side3 with accessor methods for the
three sides of a triangle.

Modify the Triangle class to throw a TriangleError exception if the three sides cannot form a
triangle. To determine if the sides make a triangle; the rule is that the sum of any two sides
must be greater than the length of the third side. Write an algorithm that performs this rule
and implement it in the TriangleError class.
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
        return f"color: {self.__color} and filled: {self.__filled}"

class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__("Invalid triangle sides!")
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise TriangleError(side1, side2, side3)
        self.__side1 = float(side1)
        self.__side2 = float(side2)
        self.__side3 = float(side3)

    def getSide1(self): return self.__side1
    def getSide2(self): return self.__side2
    def getSide3(self): return self.__side3
    def setSide1(self, side1): self.__side1 = float(side1)
    def setSide2(self, side2): self.__side2 = float(side2)
    def setSide3(self, side3): self.__side3 = float(side3)

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"{super().__str__()} side1: {self.__side1} side2: {self.__side2} side3: {self.__side3}"

def displayObject(g):
    print(g.__str__())

def main():
    try:
        s1 = float(input("Enter side1: "))
        s2 = float(input("Enter side2: "))
        s3 = float(input("Enter side3: "))
        color = input("Enter color: ")
        filled = input("Is filled? (true/false): ").strip().lower() == "true"
        t = Triangle(s1, s2, s3)
        t.setColor(color)
        t.setFilled(filled)
        print("\n---Outputs---")
        print("Area:", t.getArea())
        print("Perimeter:", t.getPerimeter())
        print("Color:", t.getColor())
        print("Is filled?", t.isFilled())
    except TriangleError as ex:
        print("\nTriangleError: Illegal side lengths!")
        print(f"Sides entered: {ex.getSide1()}, {ex.getSide2()}, {ex.getSide3()}")

if __name__ == "__main__":
    main()