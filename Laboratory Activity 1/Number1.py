"""
In-class Activity
You are creating a simple Python script that takes a distance and a completion time and outputs the speed in knots, 
miles per hour, and feet per second. Using variables write a script that defines 60 miles and a completion time of 3 hours. 
The output should show a completion speed in miles per hour, knots, and feet per second.
• The formula for calculating speed is distance/time = speed.
• To convert miles to knots, divide the miles by 1.15078.
• To convert miles to feet, multiply the miles by 5280.
• To convert hours to seconds, multiply hours by 3600.
"""
print("""
Hello User!
This python program takes a specific distance and completion time
and shows your speed in knots, miles per hour, and feet per second
The distance we're given is 60 miles with a completion time of 3 hours
""")
distance = 60
completion_time = 3
speed= distance / completion_time
knots= speed / 1.15078
feet= distance * 5280
seconds= completion_time * 3600
feet_per_seconds= f"{feet}/{seconds}"
fps= feet / seconds
print("Since we are given the values of 60 miles and 3 hours")
print("Our speed in miles per hour is", speed)
print("Our speed in knots is", knots)
print("Finally our feet per second is", feet_per_seconds, "or", fps)
