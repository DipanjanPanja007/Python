from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 23, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto( 0 , 210 )
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGN, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)