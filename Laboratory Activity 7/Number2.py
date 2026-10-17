"""
Design a class named Fan to represent a fan. The class contains:
  • Three constants named SLOW, MEDIUM, and FAST with values 1, 2, and 3 to denote the fan
    speed.
  • An int data field named speed that specifies the speed of the fan.
  • A bool data field named on that specifies whether the fan is on (default is False).
  • A float data field named radius that specifies the radius of the fan.
  • A string data field named color that specifies the color of the fan.
  • The accessor and mutator methods for all four data fields.
  • A constructor that creates a fan with the specified speed (default SLOW), radius (default 5),
    color (default blue), and on (default False).

Write a test program that creates two Fan objects. For the first object, assign the maximum
speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and
turn it off for the second object. Display each object's speed, radius, color, and on properties.
"""

class Fan:
  Slow = 1
  Medium = 2
  Fast = 3
  def __init__(self, speed=Slow, radius=5, color="blue", on=False):
    self.speed = speed
    self.radius = radius
    self.color = color
    self.on = on

# Accessor and Modifier for
# Speed
  def get_speed(self):
    return self.speed
  def set_speed(self, speed):
    self.speed = speed
# radius
  def get_radius(self):
    return self.radius
  def set_radius(self, radius):
    self.radius = radius
# color
  def get_color(self):
    return self.color
  def set_color(self, color):
    self.color = color
# on
  def get_on(self):
    return self.on
  def set_on(self, on):
    self.on = on

# TESTING----------------
fan1 = Fan()
fan1.set_speed(Fan.Fast)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

fan2 = Fan()
fan2.set_speed(Fan.Medium)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

print("Fan 1:")
print("Speed:", fan1.get_speed())
print("Radius:", fan1.get_radius())
print("Color:", fan1.get_color())
print("On:", fan1.get_on())
print()
print("Fan 2:")
print("Speed:", fan2.get_speed())
print("Radius:", fan2.get_radius())
print("Color:", fan2.get_color())
print("On:", fan2.get_on())