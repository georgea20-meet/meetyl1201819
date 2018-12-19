#problem 1 :
"""
my_name = " george "
#print(my_name)
#print(my_name*3)
#for i in range (100):
	print(my_name)
"""

#problem 2 :
"""
number1 = 30
#print(number1)
number2 = 15
#print(number2)
"""

"""
list1 = [2,6,8]
def exercise_1(x):
	
	y = x[0]
	z = x[2]
	list2 = [y,z]
	return list2

exercise_1(list1)
list2 = exercise_1(list1)
print(list2)
"""

import turtle

turtle.pensize(25)
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(100)

turtle.pensize(25)
turtle.color("black")
turtle.penup()
turtle.goto(135, -25)
turtle.pendown()
turtle.circle(100)

turtle.pensize(25)
turtle.color("red")
turtle.penup()
turtle.goto(375, -25)
turtle.pendown()
turtle.circle(100)

turtle.pensize(25)
turtle.pensize(25)
turtle.color("yellow")
turtle.penup()
turtle.goto(15, -130)
turtle.pendown()
turtle.circle(100)

turtle.pensize(25)
turtle.color("green")
turtle.penup()
turtle.goto(250, -130)
turtle.pendown()
turtle.circle(100)

turtle.done()
