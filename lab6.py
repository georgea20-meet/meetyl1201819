#exercise 1
"""
import turtle
import random
turtle.colormode(255)
from turtle import Turtle 
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random_color(self):
		R = random.randrange(0,257,10)
		G = random.randrange(0,257,10)
		B = random.randrange(0,257,10)
		self.color(R,G,B)
square00=Square(20)
square00.random_color()
turtle.mainloop()
"""

#exercise 2

