import turtle as t
from random import randrange

wn = t.Screen()
wn.title("Bouncing Balls")
wn.bgcolor("light yellow")
wn.setup(width=800, height=600)

# ball 1
ball1 = t.Turtle()
ball1.shape('circle')
ball1.color('red')
ball1.penup()
ball1.speed(0)
ball1.goto(100,0)



# ball 2
ball2 = t.Turtle()
ball2.shape('circle')
ball2.color('blue')
ball2.penup()
ball2.speed(0)
ball2.goto(-100,0)

def moveUp():
    x = ball1.xcor()
    y = ball1.ycor()
    ball1.goto(x, y+10)
def moveDown():
    x = ball1.xcor()
    y = ball1.ycor()
    ball1.goto(x, y-10)
def moveLeft():
    x = ball1.xcor()
    y = ball1.ycor()
    ball1.goto(x-10, y)
def moveRight():
    x = ball1.xcor()
    y = ball1.ycor()
    ball1.goto(x+10, y)

wn.listen()
wn.onkeypress(moveUp, 'Up')
wn.onkeypress(moveDown, 'Down')
wn.onkeypress(moveLeft, 'Left')
wn.onkeypress(moveRight, 'Right')

ball1.dx=randrange(-400, 400)
ball1.dy=randrange(-300, 300)

while True:
    wn.update()
    if ((ball1.xcor()>400 or ball1.xcor()<-400) and
     (ball1.ycor()>300 or ball1.ycor()<-300)):
        ball1.setx(ball1.xcor() - ball1.dx)
        ball1.sety(ball1.ycor() - ball1.dy)
        ball1.goto(0, 0)
        
    ball1.dx=randrange(-400, 400)
    ball1.dy=randrange(-300, 300)
    ball1.penup()
    ball1.speed(5)
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

# this is new line