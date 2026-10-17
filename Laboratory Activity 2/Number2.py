"""
Write a program that prompts the user to enter a point (x, y) and checks whether the point 
is within the circle centered at (0, 0) with radius 10. For example, (4, 5) is inside the 
circle and (9, 9) is outside the circle as shown in the figure above. A point is in the 
circle if its distance to (0, 0) is less than or equal to 10.
The formula for computing the distance is d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
"""

import math
print("This program asks for a point in the graph denoted as (x,y)")
print("then it will check if its inside the circle centered at (0,0) with a radius of 10")
x = int(input("Please input your x axis = "))
y = int(input("Please input your y axis = "))
d = math.sqrt(pow(x,2)+pow(y,2))
if d <= 10:
    print(f"Your point is located within the circle with a distance of {d}")
else:
    print("Your point is located outside the circle")