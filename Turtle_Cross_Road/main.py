from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while(game_is_on):
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) <=20 :
            game_is_on = False
            scoreboard.game_over()

    # Detect for sucess
    if player.is_road_crossed() ==True:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()

