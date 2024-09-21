from turtle import Screen
from Snake import Snake
from Food import Food
from Score_Board import Score
import time

screen = Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on=True
while(game_on):
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) <15:
        print("feed")
        snake.extend_segment()
        score.increase_score()
        food.refresh()
    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.ycor()>240 or snake.head.xcor()<-280 or snake.head.ycor()<-240 :
        score.game_over()
        game_on = False

    # detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
































