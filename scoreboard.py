from turtle import Turtle

FONT = ("Arial",20,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self) :
        super().__init__ ()
        self.score = 0
        with open("snake_game\data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.setposition(0,260)
        self.color("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} || High Score : {self.high_score}",align=ALIGNMENT,font = FONT)
        
    def reset_score(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("snake_game\data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
            
        self.score = 0 
        self.update_score() 
        
    def inc_score(self):
        self.score += 1
        self.update_score()
