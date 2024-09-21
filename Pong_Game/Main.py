import time
from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball
from Score import Score

l_paddle= Paddle((-370,0))
r_paddle=Paddle((370,0))
ball = Ball()
score = Score()

screen = Screen()
screen.bgcolor("#212121")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)




screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # ball bounced back from wall
    if ball.ycor()>=280 or ball.ycor()<=-280 :
        ball.bounce_y()

    # ball hit by player
    if (ball.xcor()==350 and ball.distance(r_paddle)<50) or (ball.xcor()==-350 and ball.distance(l_paddle)<50) :
        ball.bounce_x()

    # ball missed by right player
    if(ball.xcor()>410):
        score.l_update()
        time.sleep(0.1)
        ball.reset_position()

    # ball missed by left player
    if(ball.xcor()<-410):
        score.r_update()
        time.sleep(0.1)
        ball.reset_position()

screen.exitonclick()