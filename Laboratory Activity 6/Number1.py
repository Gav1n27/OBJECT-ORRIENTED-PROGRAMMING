"""
Write a program that reads a list of scores and then assigns grades based on the following
scheme:
    The grade is A if score is >= best - 10.
    The grade is B if score is >= best - 20.
    The grade is C if score is >= best - 30.
    The grade is D if score is >= best - 40.
    The grade is F otherwise.

Here is a sample run:
Enter scores: 40 55 70 58
Student 0 score is 40 and grade is C
Student 1 score is 55 and grade is B
Student 2 score is 70 and grade is A
Student 3 score is 58 and grade is B
"""

list = list(map(int, input("Enter scores: ").split()))
best_score = max(list)
for i, score in enumerate(list):
   if score >= best_score - 10:
       grade = "A"
   elif score >= best_score - 20:
       grade = "B"
   elif score >= best_score - 30:
       grade = "C"
   elif score >= best_score - 40:
       grade = "D"
   else:
       grade = "F"
   print(f"Student {i} score is {score} and grade is {grade}")
