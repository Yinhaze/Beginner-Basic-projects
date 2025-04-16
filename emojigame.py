import turtle

win=turtle.Screen()
win.title("emoji By Saksham Shrestha")
win.bgcolor("black")
win.setup(width=550, height=800)
win.tracer(0)

paddle=turtle.Turtle()
paddle.speed(0) #not of the paddle
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.penup()
paddle.goto(0,-350)

ball=turtle.Turtle()
ball.speed(0) #not of the paddle
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.07
ball.dy=-0.07

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0",align="center",font=("Impact",24,"normal"))


def paddle_right():
    x=paddle.xcor()
    x+=40
    paddle.setx(x)

def paddle_left():
    x=paddle.xcor()
    x-=40
    paddle.setx(x)

win.listen()
win.onkeypress(paddle_left, "a")
win.onkeypress(paddle_right, "d")
score=0

while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 400: #up
        ball.sety(400)
        ball.dy *= -1

    if ball.xcor() > 250:  # right
        ball.setx(250)
        ball.dx *= -1

    if ball.xcor() < -250:  # left
        ball.setx(-250)
        ball.dx *= -1

    if ball.ycor() < -400: #up
        pen.clear()
        pen.write("Game Over!!!!!!\n       Score:{}".format(score), align="center", font=("Impact", 24, "normal"))


    if (-340 > ball.ycor() > -350) and (paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50):
        ball.sety(-340)
        ball.dy *= -1
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Impact", 24, "normal"))





