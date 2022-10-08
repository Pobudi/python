from turtle import Turtle

START_CORDS = (-296, 50)
COLORS = {"yellow": 0, "green": 1, "orange": 2, "red": 3}


class Bricks:
    def __init__(self):
        self.bricks_data = {}

    def draw(self):
        for color in COLORS.keys():
            self.bricks_data[color] = []
            for j in range(2):
                for i in range(14):
                    diego = Turtle()
                    diego.speed("fastest")
                    diego.shape("square")
                    diego.shapesize(stretch_wid=1, stretch_len=2)
                    diego.color(color)
                    diego.penup()

                    diego.goto(START_CORDS[0]+(i * 45), START_CORDS[1]+(j*28)+(COLORS[color]*2*28))
                    self.bricks_data[color].append(diego)
