import turtle as t
import os

player_1 = 0
player_2 = 0 


#Window setup

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0)

#Left block of the game

leftp =t.Turtle()
leftp.color("yellow")
leftp.speed(0)
leftp.shape('square')
leftp.shapesize(stretch_len=1,stretch_wid=6)
leftp.penup()
leftp.goto(-350,0)

#Right block of the game

rightp = t.Turtle()
rightp.speed(0)
rightp.color("yellow")
rightp.shape('square')
rightp.shapesize(stretch_len=1,stretch_wid=6)
rightp.penup()
rightp.goto(350,0)

#Ball in the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('skyblue')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5
ball_dy = 1.5

#For updating score

pen = t.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0                    Player 2: 0 ",align="center",font=('Ariel',24,"normal"))

#Moving the blocks up and down

def leftup():
    y = leftp.ycor()
    y = y+15
    leftp.sety(y)


def leftdown():
    y = leftp.ycor()
    y = y-15
    leftp.sety(y)


def rightup():
    y = rightp.ycor()
    y = y+15
    rightp.sety(y)


def rightdown():
    y = rightp.ycor()
    y = y-15
    rightp.sety(y)


# Giving access to the keyboard

window.listen()
window.onkeypress(leftup,'u')
window.onkeypress(leftdown,'d')
window.onkeypress(rightup,'Up')
window.onkeypress(rightdown,'Down')

# Main Function

while True:
    window.update()

    # Moving the Ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    #Border setting

    if ball.ycor() > 290:   
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  
        ball.sety(-290)
        ball_dy = ball_dy * -1

    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_1 = player_1 + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(player_1,player_2),align="center",font=('Ariel',24,"normal"))
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_2 = player_2 + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(player_1,player_2),align="center",font=('Ariel',24,"normal"))
        os.system("afplay wallhit.wav&")


    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightp.ycor() + 40 and ball.ycor() > rightp.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftp.ycor() + 40 and ball.ycor() > leftp.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")



