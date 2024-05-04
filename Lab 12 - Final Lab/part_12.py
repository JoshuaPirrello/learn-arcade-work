import turtle

# first we need our classes
wn = turtle.Screen()
wn.title("Frogger Clone")
wn.setup(600, 800)
wn.bgcolor("black")

wn.register_shape('frogger_default.gif')

pen = turtle.Turtle
pen.speed(0)
pen.hideturtle()


class Sprite:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()


class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)


player = Player(0, -300, 40, 40, "frogger_default.gif")
player.render(pen)
wn.mainloop()
