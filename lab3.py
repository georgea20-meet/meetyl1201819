import turtle

turtle.register_shape("car",((50,0),(50,50),(0,50),(0.0)))

turtle.addshape("car1.gif")
turtle.shape("car1.gif")
turtle.getshapes()

for i in range (20000) :

	turtle.forward(300)
	turtle.right(50)
	turtle.forward(120)
	turtle.right(80)
	turtle.forward(60)

	turtle.mainloop()
