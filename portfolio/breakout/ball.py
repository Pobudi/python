from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(270)

        self.x_vector = 0
        self.y_vector = -5
        self.speed = 0.05

    def move(self):
        self.goto(self.xcor() + self.x_vector, self.ycor() + self.y_vector)
