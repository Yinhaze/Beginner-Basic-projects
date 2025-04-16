import turtle
import winsound

#Setup for the window of the game
win=turtle.Screen()
win.title("Pong By Saksham Shrestha")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0) #not of the paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0) #not of the paddle
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0) #not of the paddle
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.04
ball.dy=-0.04

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0  Player B: 0",align="center",font=("Impact",24,"normal"))


#score
score_a=0
score_b=0

#functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=40
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)

#keyboard
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
#win.onkeypress(paddle_b_up,"8")
#win.onkeypress(paddle_b_down,"2")

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290: #UP
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("thepong.mp3",winsound.SND_ASYNC)

    if ball.ycor() < -290: #Down
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("thepong.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:  #right
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b), align="center", font=("Impact", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0) #left
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b), align="center", font=("Impact", 24, "normal"))


    #paddle and ball
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("thepong.mp3", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("thepong.mp3", winsound.SND_ASYNC)

    if(ball.ycor() > paddle_b.ycor()):
        paddle_b_up()

    if(ball.ycor()<paddle_b.ycor()):
        paddle_b_down()



