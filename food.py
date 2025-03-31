from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = random.randint(-276, 278)
        y = random.randint(-276, 278)
        self.goto(x, y)