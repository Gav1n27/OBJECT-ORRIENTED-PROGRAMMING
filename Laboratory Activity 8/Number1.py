"""
Design the class file and implement the program that tests all methods.

BMI Class Specifications:
- Data fields:
  • name: str - The name of the person.
  • age: int - The age of the person (default is 20).
  • weight: float - The weight of the person in pounds.
  • height: float - The height of the person in inches.
- Methods:
  • BMI(name: str, age: int, weight: float, height: float) - Creates a BMI object.
  • getBMI(): float - Returns the BMI.
  • getStatus(): str - Returns the BMI status (e.g., Normal, Overweight, etc.).
"""

class BMI:
  def __init__(self, name, weight, height, age=20):
    self.name = name
    self.age = age
    self.weight = weight  # in pounds
    self.height = height  # in inches

  def getBMI(self):
    kilogramsperpound = 0.45359237
    metersperinch = 0.0254
    weightinkg = self.weight * kilogramsperpound
    heightinmeters = self.height * metersperinch
    return weightinkg / (heightinmeters**2)

  def getStatus(self):
    bmi = self.getBMI()
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# testing
person = BMI("Gavin", 160, 68, 19)
print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"BMI: {person.getBMI():.2f}")
print(f"Status: {person.getStatus()}")