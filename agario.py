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
MY_BALL = Ball(20,20,20,20,100,'black')

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


def collide(ball_a,ball_b):

	if ball_a == ball_b :

		return False 
	
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))

	if(distance + 10 < ball_a.r +ball_b.r):

		return True

	else:

		return False

def check_all_balls_collision():

	for ball_a in BALLS:
		for ball_b in BALLS:

			if collide(ball_a,ball_b) == True :

				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while dx == 0 :
					dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())

				if ball_b.r > ball_a.r :

					ball_b.r += 1
					ball_b.shapesize(ball_b.r/10)
					ball_a.r = radius
					ball_a.goto(x , y)
					ball_a.dx = dx
					ball_a.dy = dy 
					ball_a.color(color)
					ball_a.shapesize(ball_a.r/10)

				else :

					ball_a.r += 1
					ball_a.shapesize(ball_a.r/10)
					ball_b.r = radius
					ball_b.goto(x , y)
					ball_b.dx = dx
					ball_b.dy = dy 
					ball_b.color(color)
					ball_b.shapesize(ball_b.r/10)



def check_myball_collision():

	for ball in BALLS :

		
		if collide(MY_BALL,ball) == True:
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			while dx == 0 :
				dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			color = (random.random(), random.random(), random.random())

			ball_r4 = ball.r
			my_ball_r4 = MY_BALL.r



			if my_ball_r4 > ball_r4:
				ball.r = radius
				ball.x = x
				ball.y = y
				ball.goto(x , y)
				ball.dx = dx
				ball.dy = dy 
				ball.color(color)
				ball.shapesize(ball.r/10)
				MY_BALL.r = my_ball_r4 + 2
				MY_BALL.shapesize(MY_BALL.r/10)

			else:

				return False
	return True
				

def movearound(event):
	X = event.x - round(SCREEN_WIDTH)
	Y = round(SCREEN_HEIGHT) - event.y
	MY_BALL.goto(X,Y)


turtle.getcanvas().bind("<Motion>" , movearound)
turtle.listen()


while RUNNING :
	move_all_balls()
	check_all_balls_collision()
	turtle.update()

	RUNNING = check_myball_collision()

	time.sleep(SLEEP)