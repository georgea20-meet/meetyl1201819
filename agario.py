import turtle
import random
import time
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()

RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

class Ball(object):
	def __init__(self,NUMBER_OF_BALLS,MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS,MINIMUM_BALL_DX,MAXIMUM_BALL_DX,MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	