from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, -0), (-40, 0)]
MOVEMENT_SPEED = 10

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]
        self.end = self.body[len(self.body) - 1]

    def create_body(self):
        """will create the snake body"""
        for _ in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(STARTING_POSITION[_])
            self.body.append(body)

    def add_to_tail(self):
        """will add length to tail when food is eaten"""
        body_segment = Turtle("square")
        body_segment.color("white")
        body_segment.penup()
        body_segment.speed("fastest")
        end_x = self.end.xcor()
        end_y = self.end.ycor()
        body_segment.goto(end_x, end_y)
        self.body.append(body_segment)

    def move(self):
        """will let the snake to continuously move"""
        for segment in range(len(self.body) - 1, 0, - 1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.forward(MOVEMENT_SPEED)

    def go_up(self):
        """will let the snake go up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """will let the snake go down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        """will let the snake go left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        """will let the snake go right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
