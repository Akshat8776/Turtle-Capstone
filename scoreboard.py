from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.levelup()
        
    def levelup(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.level+=1
        self.write(f"Level: {self.level}",align="left",font=FONT)
        
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
