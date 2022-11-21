from turtle import Turtle, Screen
import time 
from snake import Snake
from food import Food 
from scoreboard import Scoreboard 

FONT_MAIN = ("Courier",20,"normal")
ALIGNMENT = "center"

turt = Turtle()

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food) < 15:  
        food.refresh() 
        snake.extend() 
        scoreboard.inc_score()
        
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_on = False
        print("GAME OVER") 
        scoreboard.game_over()
        
   
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
        
screen.exitonclick()
