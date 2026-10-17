"""
Matthew is preparing special dishes for his daughter's birthday. It takes him a minutes to
prepare the first dish, and each following dish takes b minutes longer than the previous
dish. He has t minutes to prepare the dishes. For example, if the first dish takes a=10
minutes and b=5, then the second dish will take 15 minutes, the third dish will take
20 minutes, and so on. If he has 80 minutes to prepare the dishes, then he can prepare
four dishes because 10+15+20+25=70. Write a program that prompts the user to
enter the values of a, b, and t, and outputs the number of dishes Matthew can prepare.
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
t = int(input("Enter t: "))

count = 0
current_time = a

while t >= current_time:
    t -= current_time
    count += 1
    current_time += b

print(count)