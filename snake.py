from turtle import Turtle

POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACES=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POINTS:
            self.add_segments(position)

    def add_segments(self,position):
        tim = Turtle("square")
        tim.penup()
        tim.color("green")
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)

        self.head.fd(MOVE_DISTACES)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

