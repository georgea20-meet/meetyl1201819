import turtle
import random
import time
import math
from Ball import Ball

turtle.tracer(0)
turtle.hideturtle()

RUNNING = True 
SLEEP = 0.00077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS) :
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while dx == 0 :
		dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())

	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls() :

	for new_ball in BALLS :

		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

while RUNNING :
	move_all_balls()
	turtle.update()
	time.sleep(SLEEP)

def collide(self,ball_a,ball_b):

	if ball_a == ball_b :

		return False 
	
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))

	if(distance + 10 < ball_a.r +ball_b.r):

		return True

	else:

		return False

def check_all_balls_collision():

	for ball_a in BALLS :

	for ball_b in BALLS :

	if collide(ball_a,ball_b) == True :

		ball_a_radius = ball_a.r
		ball_b_radius = ball_a.r

X_COORDINATE = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
Y_COORDINATE = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

while X_AXISSPEED == 0 or Y_AXISSPEED == 0 :

	X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
	Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

radius =random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
color = (random.random(),random.random(),random.random())

my_ball = Ball(0,0,10,10,10,"Balck")

def check_myball_collision():

	for ball in BALLS :

		if collide(ball , my_ball):

			R1 = ball.r




