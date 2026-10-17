"""
Use nested loops to display the following patterns:
Pattern A    Pattern B    Pattern C    Pattern D
1            1 2 3 4 5 6          1    1 2 3 4 5 6
1 2          1 2 3 4 5          2 1      1 2 3 4 5
1 2 3        1 2 3 4          3 2 1        1 2 3 4
1 2 3 4      1 2            4 3 2 1          1 2 3
1 2 3 4 5    1            5 4 3 2 1            1 2
1 2 3 4 5 6             6 5 4 3 2 1              1
"""

print("\nPattern A:")
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern B:")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern C:")
for i in range(1, 7):
    print(" " * (6 - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPattern D:")
for i in range(6, 0, -1):
    print(" " * (6 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()