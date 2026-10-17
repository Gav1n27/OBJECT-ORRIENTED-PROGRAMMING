"""
Write the following function to display an integer in reverse order: def reverse(number).
For example, reverse(3456) displays 6543. Write a test program that prompts the user
to enter an integer and displays its reversal.
"""

numbers = (input("Please input integers:" ))
def reverse(numbers):
    return numbers[::-1]
    
print(f"The reverse of your integers is {reverse(numbers)}")