from turtle import Turtle,Screen
STARTING_POSITION = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
    """  When you append a new segment to the self.segments list using self.segments.append(segment), it gets added to the end 
            of the list. Here’s how the process works:
           1. Current Last Position: When you call self.segments[-1].position(), you're getting the coordinates of the last segment in the snake.
           2. Appending New Segment: In the extend_segment method, self.add_segment(self.segments[-1].position()) creates a new segment 
                and positions it at the coordinates of the last segment.
           3. Visual Placement: Even though you’re placing the new segment at the same coordinates as the last segment, it's appended to the end of the self.segments list. This means that in the next move, the newly added segment will follow the last segment’s movement, effectively extending the snake. """

    def move(self):
        for seg_num in range(len(self.segments)-1 ,  0 ,  -1):
             new_x = self.segments[seg_num - 1].xcor()
             new_y = self.segments[seg_num - 1].ycor()
             self.segments[seg_num].goto((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


