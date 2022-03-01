import turtle

arr=["blue", "purple", "cyan", "green"]
counter = 0
counter2 = 0
window=turtle.Screen()
window.title("mobarak is here")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#right stick
right_stick=turtle.Turtle()
right_stick.speed(0)
right_stick.shape("square")
right_stick.color("white")
right_stick.shapesize(stretch_wid=5, stretch_len=1)
right_stick.penup()
right_stick.goto(350, 0)
#left stick
left_stick=turtle.Turtle()
left_stick.speed(0)
left_stick.shape("square")
left_stick.color("white")
left_stick.shapesize(stretch_wid=5, stretch_len=1)
left_stick.penup()
left_stick.goto(-350, 0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5
#left stick up
def left_stick_up():
    y=left_stick.ycor()
    y+=20
    left_stick.sety(y)
#left stick down
def left_stick_down():
    y=left_stick.ycor()
    y-=20
    left_stick.sety(y)
#right stick up
def right_stick_up():
    y = right_stick.ycor()
    y += 20
    right_stick.sety(y)

# right stick down
def right_stick_down():
    y = right_stick.ycor()
    y -= 20
    right_stick.sety(y)
window.listen()
window.onkeypress(left_stick_up, "w")
window.onkeypress(left_stick_down, "s")
window.onkeypress(right_stick_up, "Up")
window.onkeypress(right_stick_down, "Down")

score_a=0
score_b=0

#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


#main game loop
while True:
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("player A: {}  player B: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -340 and (ball.ycor() < left_stick.ycor() + 40 and ball.ycor() > left_stick.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        counter2 += 1
        if counter2 > 3:
            counter2 = 0
        left_stick.color(arr[counter])
    if ball.xcor() > 340 and (ball.ycor() < right_stick.ycor() + 40 and ball.ycor() > right_stick.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        counter += 1
        if counter > 3:
            counter = 0
        right_stick.color(arr[counter])
