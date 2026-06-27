from turtle import Turtle,Screen
from Paddle import paddle
from Ball import ball
from score import Scoreboard
import time



screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=paddle(350,0)
l_paddle=paddle(-350,0)
score=Scoreboard()
ball=ball()

   

def up_r():
    new_y=r_paddle.ycor()+20
    r_paddle.goto(r_paddle.xcor(),new_y)
    

def down_r():
    new_y=r_paddle.ycor()-20
    r_paddle.goto(r_paddle.xcor(),new_y)
    

def up_l():
    new_y=l_paddle.ycor()+20
    l_paddle.goto(l_paddle.xcor(),new_y)
    

def down_l():
    new_y=l_paddle.ycor()-20
    l_paddle.goto(l_paddle.xcor(),new_y)
    

screen.listen()
screen.onkeypress(up_r,"Up")
screen.onkeypress(down_r,"Down")
screen.onkeypress(up_l,"w")
screen.onkeypress(down_l,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() 

    #detect collison with wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()

    # DETECT collison with r_paddle
    if ball.distance(r_paddle) <50 and ball.xcor()>320: 
        ball.bounce_x()
        score.r_update_score()

    if ball.distance(l_paddle) <50 and ball.xcor()<-320:
        ball.bounce_x()
        score.l_update_score()

    if ball.xcor()>380:
        ball.reset_pos()

    if ball.xcor()<-380:
        ball.reset_pos()
























screen.exitonclick()