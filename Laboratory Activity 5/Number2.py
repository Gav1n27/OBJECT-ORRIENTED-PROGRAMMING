"""
Write a program that generates a text file containing an unspecified number of scores (integers), up
to a maximum of 500 scores. Each score must be between 0 and 100 (inclusive). Scores should be
separated by spaces (a single line is acceptable):
  • The highest and lowest score.
  • The number of occurrences of the highest and lowest score.
  • The average score (to 2 decimal places).
  • The count of scores in each range: 0–59, 60–79, 80–89, 90–100.

Display all valid scores, separated by spaces, in the order they appear in the file. Your program
should prompt the user to enter a filename.
"""

import random
filename = input("Enter filename: ")
filename = "/tmp/" + filename
num_scores = int(input("How many scores (1-500): "))
if num_scores < 1:
    num_scores = 1
if num_scores > 500:
    num_scores = 500
scores = []
for i in range(num_scores):
    scores.append(random.randint(0, 100))
file = open(filename, "w")
file.write(" ".join(str(s) for s in scores))
file.close()
file = open(filename, "r")
content = file.read()
file.close()
valid_scores = []
for word in content.split():
    num = int(word)
    if 0 <= num <= 100:
        valid_scores.append(num)
print("Scores:", " ".join(str(s) for s in valid_scores))
highest = valid_scores[0]
lowest = valid_scores[0]
for s in valid_scores:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s
high_count = 0
low_count = 0
for s in valid_scores:
    if s == highest:
        high_count += 1
    if s == lowest:
        low_count += 1
total = 0
for s in valid_scores:
    total += s
average = total / len(valid_scores)
range1 = 0
range2 = 0
range3 = 0
range4 = 0
for s in valid_scores:
    if s <= 59:
        range1 += 1
    elif s <= 79:
        range2 += 1
    elif s <= 89:
        range3 += 1
    else:
        range4 += 1
print("Highest score:", highest, "| Occurrences:", high_count)
print("Lowest score:", lowest, "| Occurrences:", low_count)
print("Average score:", "%.2f" % average)
print("0-59:", range1)
print("60-79:", range2)
print("80-89:", range3)
print("90-100:", range4)