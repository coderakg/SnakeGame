from turtle import Turtle, Screen
import time 
from snake import Snake
from food import Food 
from scoreboard import Scoreboard 

FONT_MAIN = ("Uncracked",20,"normal")
ALIGNMENT = "center"

#initialising turtle object from the module
turt = Turtle()

#initialising screen from Screen object and screen settings
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #tracer function is used to turn the animation on or off and set a delay for update drawings.
# start_pos = [(0,0), (-20,0), (-40,0)]

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True

#since we have turned the animation tracer off, we will manually update and then move the snake using a while loop
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    #Detecting collision with food
    if snake.head.distance(food) < 15: # using the distance method from turtle, we take the head of snake to 
        food.refresh() # when the snake collides with the food the position refreshes
        snake.extend() # everytime there is a collision with food the snake will extend
        scoreboard.inc_score()
        
    #DETECT collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_on = False
        print("GAME OVER") 
        scoreboard.game_over()
        
    #detect tail collision here
    #loop throught the snake segements and checking their distance 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: #only in this case we will have the snake head == currrent snake segment
            game_on = False
            scoreboard.game_over()
        
screen.exitonclick()
