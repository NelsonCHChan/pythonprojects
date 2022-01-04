# Pong Game
import turtle

wn = turtle.Screen()
wn.title("Pong by Nelson Chan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Set the ball's initial movement speed and direction.
dx, dy = 2, 2

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        dx *= -1

    # Paddle and ball collisions
    if 340 < ball.xcor() < 350 and (
        paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60
    ):
        ball.setx(340)
        dx *= -1

    if -350 < ball.xcor() < -340 and (
        paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60
    ):
        ball.setx(-340)
        dx *= -1
