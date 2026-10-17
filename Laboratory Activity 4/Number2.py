"""
Write the following function to display three numbers in increasing order: def
displaySortedNumbers (num1, num2, num3). Write a test program that prompts the
user to enter three numbers and invokes the function to display them in increasing
order.
"""

num1 = input("enter your first number: ")
num2 = input("enter your second number: ")
num3 = input("enter your third number: ")
def displaySortedNumbers(num1, num2, num3):
    sortednumbers = sorted([num1, num2, num3])
    print(f"{sortednumbers[0]}, {sortednumbers[1]}, {sortednumbers[2]}")
displaySortedNumbers(num1, num2, num3)