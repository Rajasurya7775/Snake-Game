from turtle import Screen
import time as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

positions = [(0,0),(-20,0),(-40,0)]
segments = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on = True

while is_game_on:
    screen.update()
    t.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>285 or snake.head.xcor() < -285 or snake.head.ycor() >285 or snake.head.ycor()<-285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:                     #[1:] --> to avoid the head collised with itself
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()