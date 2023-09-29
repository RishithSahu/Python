import turtle
import random
import time

def atLeftEdge(ball,screen_width):
    if ball.xcor() < -screen_width/2:
         return True
    else:
         return False

def atRightEdge(ball,screen_width):
    if ball.xcor() > screen_width/2:
         return True
    else:
         return False

def atTopEdge(ball,screen_height):
    if ball.ycor() > screen_height/2:
         return True
    else:
         return False

def atBottomEdge(ball,screen_height):
    if ball.ycor() < -screen_height/2:
         return True
    else:
         return False

def bounceball(ball, new_direction):
     if new_direction == "left" or new_direction == "right":
          new_heading = 180 - ball.heading()
     elif new_direction == "down" or new_direction == "up":
          new_heading = 360 - ball.heading()
     return new_heading

def createBalls(num_balls):
     balls = []
     for k in range(0,num_balls):
          new_ball = turtle.Turtle()
          new_ball.shape("circle")
          new_ball.fillcolor("black")
          new_ball.speed(0)
          new_ball.penup()
          new_ball.setheading(random.randint(1,359))
          balls.append(new_ball)
     return balls

print("A program to simulate bouncing balls on a screen")

turtle.setup(800,600)
wind = turtle.Screen()
wind.title("Bouncling Balls")
numball = int(input("Total number of balls to be simulated : "))
numsec = int(input("Total number of seconds to be simulated for : "))

balls = createBalls(numball)
start_time = time.time()
terminate = False
while not terminate:
     for k in range(0,len(balls)):
        balls[k].forward(15)

        if atLeftEdge(balls[k],800):
             balls[k].setheading(bounceball(balls[k],"right"))
        elif atRightEdge(balls[k],800):
             balls[k].setheading(bounceball(balls[k],"left"))
        elif atTopEdge(balls[k],600):
             balls[k].setheading(bounceball(balls[k],"down"))
        elif atBottomEdge(balls[k],600):
             balls[k].setheading(bounceball(balls[k],"up"))
        if time.time() - start_time > numsec:
             terminate = True


