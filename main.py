import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
c=CarManager()
sc=Scoreboard()
screen.listen()
screen.onkey(player.goup,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.gameover():
        player.gotostart()
        c.speed()
        sc.levelup()
    c.createcar()
    c.move()
    for car in c.cars:
        if car.distance(player)<=20:
            game_is_on = False
sc.gameover()
print(f"You failed to cross level {sc.level}")
screen.exitonclick()
    
    
    
