"""
Zeller's congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is:
h = (q + floor(26(m + 1) / 10) + k + floor(k / 4) + floor(j / 4) + 5j) % 7
Where h is the day of the week (0: Saturday, 1: Sunday, etc), q is the day of the month, m is the month 
(3: March, 4: April,..., 12: December), January and February are counted as months 13 and 14 of the previous year; 
j is the century (year / 100), and k is year of the century (year % 100).
Write a program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week.
"""

print("""
This program prompts the user to enter a year, month, and day of the month
and then it displays the name of the day of the week!
""")
year = int(input("Enter year (ex: 2026): "))
m = int(input("Enter month (ex: 1-12): "))
q = int(input("Enter day of the month (ex: 1-31): "))
if m == 1 or m == 2:
    m += 12
    year -= 1
j= year//100
k= year%100
h = (q + (26 * (m + 1)) // 10 + k + (k // 4) + (j // 4) + (5 * j)) % 7
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The day of the week is {days[h]}")