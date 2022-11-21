# the food file will contain a class food that will create small dot that will be the food object
# the food will re appear each time the snake eats it in a new location

colors = ["red","white","light blue","pink"]

from turtle import Turtle
import random
# making a good class that will inherit from the turtle class
class Food(Turtle):
    def __init__(self) :
        super().__init__() # inheriting the turtle class with the super 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color(random.choice(colors))
        self.speed("fastest") # to avoid watching the animation
        self.refresh()
         # the position of the food will be decided randomly

        
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)