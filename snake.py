from turtle import Turtle
# to make the code base better and more object oriented we will use oop to make the snake game. 

#We start by making another file snake.py 

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0  

class Snake:
    #init constructor defines what will happen to the new snake object 
    def __init__(self) :
        self.segments = [] #new attribute associated with our snake class
        self.create_snake() # a new method to create the snake
        self.head = self.segments[0] #snake head is a variable that we will use again and again, so we have made another attribute
        
        #the function to create a snake
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position) # the for loop to keep adding the segment to the position that we have specified
            
        #function to make the snake move
    #this function will keep adding another segment/square to the snake 
    def add_segment(self,position): #position is where the snake will add the new segment
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position) # taking the position
        self.segments.append(new_segment)
        
    def extend(self):
        #this function will extend the snake everytime it eats food
        self.add_segment(self.segments[-1].position()) #starting from the end of the list and then using that to hold its position
        
    def move(self):
        for seg_num in range(len(self.segments) - 1 , 0, -1): # if we have to count back in range we can use the -1 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y )   
        self.head.forward(MOVE_DIST)

#definind direction functions and since the snake is not allowed to move in a completely opposite direction we have to set if statements.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
