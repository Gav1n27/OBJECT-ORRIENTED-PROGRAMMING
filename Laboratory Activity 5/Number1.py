"""
An ISBN-10 consists of 10 digits: d1 d2 d3 d4 d5 d6 d7 d8 d9 d10. The last digit d10 is a checksum, which is
calculated from the other nine digits using the following formula:

(d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11

If the checksum is 10, the last digit is denoted as X, according to the ISBN convention. Write a
program that prompts the user to enter the first 9 digits as a string and displays the 10-digit ISBN
(including leading zeros). The program should read the input as a string.
"""

d = str(input("Please input 9 digits: "))
length = len(d)
if length > 9:
  print("Please input 9 digits only")
elif length < 9:
  print("Please input 9 digits only")
d1_string = d[0]
d2_string = d[1]
d3_string = d[2]
d4_string = d[3]
d5_string = d[4]
d6_string = d[5]
d7_string = d[6]
d8_string = d[7]
d9_string = d[8]
d1 = int(d1_string)
d2 = int(d2_string)
d3 = int(d3_string)
d4 = int(d4_string)
d5 = int(d5_string)
d6 = int(d6_string)
d7 = int(d7_string)
d8 = int(d8_string)
d9 = int(d9_string)
d10 = (d1*1 + d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 +d9*9) % 11
if d10 == 10:
  d10 = "X"
else:
  d10 = d10
print(f"The ISBN-10 number is {d}{d10}")