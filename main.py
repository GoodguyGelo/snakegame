from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("THE SNAKE GAME")

snake = Snake()
scoreboard = Scoreboard()
food = Food()

# movement controls
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food a new food after
    if food.distance(snake.head) <= 10:
        food.generate_food()
        snake.add_to_tail()
        scoreboard.update_score()

    # detect collision with wall
    if snake.head.xcor() >= 295 or snake.head.xcor() <=-295 or snake.head.ycor() <= -295 or snake.head.ycor() >= 295:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.body[2:len(snake.body)]:
        if snake.head.distance(segment) <= 5:
            game_is_on = False
            scoreboard.game_over()












screen.exitonclick()