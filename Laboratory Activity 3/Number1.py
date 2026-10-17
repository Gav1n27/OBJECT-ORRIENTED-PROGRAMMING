"""
Write a program using while loop that reads an unspecified number of integers,
determines how many positive and negative values have been read, and computes the
total and average of the input values (not counting zeroes). The program ends with the
input 0.
"""

pos_count = 0
neg_count = 0
total_sum = 0
total_count = 0

number = int(input("Please Input an Integer (0 will end the program): "))

while number != 0:
    if number > 0:
        pos_count += 1
    elif number < 0:
        neg_count += 1
    total_sum += number
    total_count += 1
    number = int(input("Please Input another Integer (0 will end the program): "))

if total_count > 0:
    average = total_sum / total_count
    print(f"Positives: {pos_count}, Negatives: {neg_count}")
    print("Total Sum:", total_sum)
    print("Average:", average)
else:
    print("No numbers were entered.")