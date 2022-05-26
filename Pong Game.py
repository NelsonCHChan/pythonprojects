"""Pong Game."""

import turtle

HEIGHT = 600
WIDTH = 800

PADDLE_X_POS = int(WIDTH / 2) - 50
PADDLE_DY = 20
PADDLE_STRETCH_WID = 5
PADDLE_STRETCH_LEN = 1
PADDLE_LEN = PADDLE_STRETCH_WID * 10
PADDLE_COLOUR = "white"
PADDLE_SHAPE = "square"

BALL_X_LIM, BALL_Y_LIM = (390, 290)
BALL_COLOUR = "white"
BALL_SHAPE = "square"


wn = turtle.Screen()
wn.title("Pong by Nelson Chan")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape(PADDLE_SHAPE)
paddle_a.color(PADDLE_COLOUR)
paddle_a.shapesize(
    stretch_wid=PADDLE_STRETCH_WID,
    stretch_len=PADDLE_STRETCH_LEN,
)
paddle_a.penup()
paddle_a.goto(-PADDLE_X_POS, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape(PADDLE_SHAPE)
paddle_b.color(PADDLE_COLOUR)
paddle_b.shapesize(
    stretch_wid=PADDLE_STRETCH_WID,
    stretch_len=PADDLE_STRETCH_LEN,
)
paddle_b.penup()
paddle_b.goto(PADDLE_X_POS, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


def paddle_a_up():
    new_y = paddle_a.ycor() + PADDLE_DY
    paddle_a.sety(new_y)


def paddle_a_down():
    new_y = paddle_a.ycor() - PADDLE_DY
    paddle_a.sety(new_y)


def paddle_b_up():
    new_y = paddle_b.ycor() + PADDLE_DY
    paddle_b.sety(new_y)


def paddle_b_down():
    new_y = paddle_b.ycor() - PADDLE_DY
    paddle_b.sety(new_y)


# Keyboard binding.
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

ball_dx = 2
ball_dy = 2

# Main game loop.
while True:
    wn.update()

    # Move the ball.
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Paddle A and ball collisions.
    cond1 = -PADDLE_X_POS < ball.xcor() < -PADDLE_X_POS + 10
    cond2 = paddle_a.ycor() - PADDLE_LEN < ball.ycor() < paddle_a.ycor() + PADDLE_LEN

    # Paddle B and ball collisions.
    cond3 = PADDLE_X_POS - 10 < ball.xcor() < PADDLE_X_POS
    cond4 = paddle_b.ycor() - PADDLE_LEN < ball.ycor() < paddle_b.ycor() + PADDLE_LEN

    # Border checking.
    if ball.ycor() > BALL_Y_LIM:
        ball.sety(BALL_Y_LIM)
        ball_dy *= -1
    elif ball.ycor() < -BALL_Y_LIM:
        ball.sety(-BALL_Y_LIM)
        ball_dy *= -1
    elif (ball.xcor() > BALL_X_LIM) or (ball.xcor() < -BALL_X_LIM):
        ball.goto(0, 0)
        ball_dx *= -1
    elif cond1 and cond2:
        ball.setx(-PADDLE_X_POS + 10)
        ball_dx *= -1
    elif cond3 and cond4:
        ball.setx(PADDLE_X_POS - 10)
        ball_dx *= -1
