from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Comic sans", 30, "normal"))

    def l_update(self):
        self.l_score+=1
        self.update_score()
    def r_update(self):
        self.r_score+=1
        self.update_score()
