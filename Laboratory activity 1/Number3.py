"""
An employee's total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. 
Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs 
the hourly wage, total regular hours, and total overtime hours and displays an employee's total weekly pay
"""

print("Hello user! we will compute your total weekly pay!")
hourlywage = float(input("Enter the hourly wage: "))
regularhours = float(input("Enter total regular hours: "))
overtimehours = float(input("Enter total overtime hours: "))
regularpay = hourlywage * regularhours
overtimepay = overtimehours * (1.5 * hourlywage)
totalpay = regularpay + overtimepay
print(f"The employee's total weekly pay is: ${totalpay}")
