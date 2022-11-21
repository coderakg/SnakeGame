from turtle import Turtle

FONT = ("Arial",20,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self) :
        super().__init__ ()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0,260)
        self.color("white")
        self.update_score()
        
    def update_score(self):
        self.write(f"Score : {self.score}",align=ALIGNMENT,font = FONT)
        
    def game_over(self):
        self.color("red")
        self.setposition(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font = ("Courier",50,"normal"))
        self.setposition(0,-60)
        self.write(f"Final Score: {self.score}",align=ALIGNMENT,font = ("Indie Flower",50,"normal"))
        
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()