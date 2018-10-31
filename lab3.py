import turtle

turtle.register_shape("car",((50,0),(50,50),(0,50),(0.0)))

turtle.addshape("car1.gif")
turtle.shape("car1.gif")
turtle.getshapes()

for i in range (360) :

	turtle.speed(180)
	turtle.right(i)
	turtle.forward(300)
	turtle.right(40)
	turtle.forward(120)
	turtle.right(100)
	turtle.forward(80)		
	turtle.home()



turtle.mainloop()