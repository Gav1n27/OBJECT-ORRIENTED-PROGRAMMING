"""
Write a program with a functions that allows the user to enter a decimal input with a
maximum value of 1023. The program then converts the decimal input into its
hexadecimal value. Example, if the user enter 15; the value will be 0FF. The program
will have a maximum value of 3FF (which is the value of 1023 when converted to
hexadecimal).
"""

number = int(input("Enter your number: "))
if number > 1023:
    print("Please input a number lower than 1023")
else:
    def convert(number):
        number = int(number)
        hexadecimal = hex(number)
        return hexadecimal
        
print(convert(number))