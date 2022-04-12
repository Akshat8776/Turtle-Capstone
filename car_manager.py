from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        self.cspeed=10
        
    def createcar(self):
        r=random.randint(1,4)
        if r==1:
            newcar=Turtle("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            rnd_y=random.randint(-250,250)
            newcar.goto(300,rnd_y)
            self.cars.append(newcar)
        
    def move(self):
        for car in self.cars:
            car.backward(self.cspeed)
            if car.xcor()==-320:
                self.cars.remove(car)
                
    def speed(self):
        self.cspeed+=5
            