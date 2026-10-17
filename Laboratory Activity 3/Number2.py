"""
The greatest common divisor (GCD) of the two integers 4 and 2 is 2. The GCD of 16 and
24 is 8. Write a program that takes two integers as inputs and displays the GCD for both
inputs.
"""

print("Please input 2 integers!")
num1 = int(input("Please Your First Integer: "))
num2 = int(input("Please Your Second Integer: "))

number1 = num1
number2 = num2

while number2 != 0:
    remainder = number1 % number2
    number1 = number2
    number2 = remainder

print(f"The GCD of {num1} and {num2} is {number1}")