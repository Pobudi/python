from turtle import Turtle

MOVING, DRAGGING = (0, 1)
# I was unable to write my own code to make turtle follow my cursor (it crashed after ~20 seconds) so i had to use
# @cdlane answer under this stackoverflow post: https://stackoverflow.com/questions/44599226/move-python-turtle-with-mouse-pointer/44601555#44601555


class Paddle(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.shape('square')
        self.hideturtle()

        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.speed('fastest')
        self.penup()
        self.setheading(self.towards(0, -300))
        self.goto(0, -300)
        self.showturtle()

        self.state = MOVING

        self.onmove(screen, self.move_handler)  # a la screen.onmove(move_handler)

    def move_handler(self, x):
        if self.state != MOVING:  # ignore stray events
            return

        self.onmove(self.screen, None)  # avoid overlapping events

        self.setheading(self.towards(x, -300))

        self.goto(x, -300)
        self.onmove(self.screen, self.move_handler)

    def onmove(self, screen, fun):
        if fun is None:
            screen.cv.unbind('<Motion>')
        else:
            def eventfun(event):
                fun(screen.cv.canvasx(event.x) / screen.xscale)
            screen.cv.bind('<Motion>', eventfun)
