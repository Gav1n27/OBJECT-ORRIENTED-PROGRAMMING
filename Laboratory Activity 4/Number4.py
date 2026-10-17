"""
Write a program with a function that displays an n-by-n matrix using the following
header: def printMatrix(n). Each element is 0 or 1, which is generated randomly.
"""

import random
def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0, 1), end=" ")
        print() 
n = int(input("Enter the value for n: "))
printMatrix(n)