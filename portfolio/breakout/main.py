from turtle import Screen
from bricks import Bricks
from paddle import Paddle
from score import Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=640, height=750)
screen.bgcolor("black")
screen.title("Breakout")
screen.listen()

screen.tracer(False)
score = Score()
score.update()

wall = Bricks()
wall.draw()
bricks_data = wall.bricks_data

paddle = Paddle(screen)
ball = Ball()

game_on = True
hits = 0
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.speed)

    # checking if the ball touched the paddle
    if ball.distance(paddle) <= 53 and ball.ycor() <= -289.5:
        # checking which part of paddle the ball touched
        paddle_centre = paddle.xcor()
        ball_centre = ball.xcor()
        if ball_centre < paddle_centre:
            ball.x_vector = -5
        elif ball_centre > paddle_centre:
            ball.x_vector = 5
        else:
            ball.x_vector = 0
        ball.y_vector *= -1

    # checking if the ball has touched any of the side walls
    elif ball.xcor() >= 309 or ball.xcor() <= -309:
        ball.x_vector *= -1

    # checking if the ball has touched the roof
    elif ball.ycor() >= 364:
        ball.y_vector *= -1

    # checking if the ball hadn't fallen out of the game
    elif ball.ycor() < -375:
        score.game_over()
        game_on = False

    # checking if the ball touched any of the bricks
    elif ball.ycor() >= 35:
        for color in bricks_data.keys():
            for index, brick in enumerate(bricks_data[color]):
                if ball.distance(brick) <= 30:

                    # if the ball hits left or right side of the brick
                    if brick.ycor() - 10.5 < ball.ycor() < brick.ycor() + 10.5:
                        ball.x_vector *= -1
                    # if the ball hits up or down of the brick
                    else:
                        ball.y_vector *= -1

                    # deleting brick from screen
                    brick.hideturtle()
                    bricks_data[color].pop(index)

                    # Increasing score according to original atari breakout rules
                    score.score += score.points[color]
                    score.update()

                    # Increasing speed also according to original atari breakout rules
                    hits += 1
                    if hits == 4 or hits == 12 or len(bricks_data["orange"]) == 27 or len(bricks_data["red"]) == 27:
                        ball.speed *= 0.01

screen.mainloop()
