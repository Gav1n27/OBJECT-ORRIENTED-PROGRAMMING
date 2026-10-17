"""
Write a program that reads integers, finds the largest of them, and counts its occurrences.
Assume that the input ends with number 0. Suppose you entered 3 5 2 5 5 5 0; the program
finds that the largest number is 5 and the occurrence count for 5 is 4.
"""

largest = None
count = 0

while True:
    n = int(input("Enter a number (0: for end of input): "))
    if n == 0:
        break
    if largest is None or n > largest:
        largest = n
        count = 1
    elif n == largest:
        count += 1

if largest is not None:
    print(f"The largest number is {largest}")
    print(f"The occurrence count of the largest number is {count}")