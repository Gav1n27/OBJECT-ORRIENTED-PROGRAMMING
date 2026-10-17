"""
Write a program that requests three scores as input and displays the average 
of the two highest scores. For example:

Enter first score: 85
Enter second score: 93
Enter third score: 91
Average of two highest scores is 92.00
"""

print("This program displays requests 3 scores and it will calculate and display the average of the 2 highest scores")
First = int(input("Please input your first score = "))
Second = int(input("Please input your second score = "))
Third = int(input("Please input your third score = "))
if First < Second and Second < Third:
    Highest_1 = Third
    Highest_2 = Second
elif First < Third and Third < Second:
    Highest_1 = Second
    Highest_2 = Third
elif Second < First and First < Third:
    Highest_1 = Third
    Highest_2 = First
elif Second < Third and Third < First:
    Highest_1 = First
    Highest_2 = Third
elif Third < First and First < Second:
    Highest_1 = Second
    Highest_2 = First
else:
    Highest_1 = First
    Highest_2 = Second
average = (Highest_1 + Highest_2) / 2
print("The average of your two highest scores is = ", average)
