from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = {"yellow": 1, "green": 3, "orange": 5, "red": 7}
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

    def update(self):
        self.clear()
        self.setposition(0, 270)
        self.write(self.score, align='center', font=("Courier", 70, "normal"))

    def game_over(self):
        self.setposition(0, -80)
        self.write("GAME OVER", align='center', font=("Courier", 90, "normal"))