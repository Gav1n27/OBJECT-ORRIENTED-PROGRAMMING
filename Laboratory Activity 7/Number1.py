"""
Design a class named Rectangle to represent a rectangle. The class contains:
  • Two data fields named width and height.
  • A constructor that creates a rectangle with the specified width and height. The default
    values are 1 and 2 for the width and height, respectively.
  • A method named getArea() that returns the area of the rectangle.
  • A method named getPerimeter() that returns the perimeter.
  • Mutator methods named setWidth() and setHeight() that changes the values of the width
    and height, respectively.
  • Accessor methods named getWidth() and getHeight() that prints the values of the width
    and height, respectively.

Draw the UML diagram for the class and then write a program that implements the class
with two Rectangle objects. Test out all the methods of the Rectangle class.
"""

class Rectangle:
  def __init__(self, width=1, height=2):
    self.width = width
    self.height = height
  def getArea(self):
    return self.width * self.height
  def getPerimeter(self):
    return 2 * (self.width + self.height)
  def setHeight(self, height):
    self.height = height
  def setWidth(self, width):
    self.width = width
  def getHeight(self):
    return self.height
  def getWidth(self):
    return self.width

# testing part
rectangle1 = Rectangle()
rectangle2 = Rectangle(5,10)
print("==== Rectangle 1 ====")
print("Width:", rectangle1.getWidth())
print("Height:", rectangle1.getHeight())
print("Area:", rectangle1.getArea())
print("Perimeter:", rectangle1.getPerimeter())
print("==== Changing Rectangle 1 ====")
rectangle1.setWidth(7)
rectangle1.setHeight(8)
print("New Width:", rectangle1.getWidth())
print("New Height:", rectangle1.getHeight())
print("New Area:", rectangle1.getArea())
print("New Perimeter:", rectangle1.getPerimeter())
print("==== Rectangle 2 ====")
print("Width:", rectangle2.getWidth())
print("Height:", rectangle2.getHeight())
print("Area:", rectangle2.getArea())
print("Perimeter:", rectangle2.getPerimeter())