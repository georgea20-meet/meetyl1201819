import turtle

for i in range (5) :

	turtle.forward(300)
	turtle.left(216)

turtle.begin_fill()
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

turtle.mainloop()
