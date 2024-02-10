import turtle as t
# Score varibales
player_a_score = 0
player_b_score = 0
a= t.Screen()    # creating a window
a.title("Ping-Pong Game") # Giving name to the game.
a.bgcolor('black')    # providing color to the HomeScreen
a.setup(width=800,height=600) # Size of the game pane
a.tracer(0)   # which speed up's the game.
# Creating left block for the game
block_left = t.Turtle()
block_left.speed(0)
block_left.shape('square')
block_left.color('yellow')
block_left.shapesize(stretch_wid=5,stretch_len=1)
block_left.penup()
block_left.goto(-350,0)
# Creating a right block for the game
block_right = t.Turtle()
block_right.speed(0)
block_right.shape('square')
block_right.shapesize(stretch_wid=5,stretch_len=1)
block_right.color('yellow')
block_right.penup()
block_right.goto(350,0)
# Creating a pong ball for the game
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_dx = 0.17  # Setting up the pixels for the ball movement.
ball_dy = 0.17 # Creating a pen for updating the Score
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=("Comic Sans MS",24,"normal"))
# Moving the left block using the keyboard
def block_left_up():
    y = block_left.ycor()
    y = y + 25
    block_left.sety(y)
# Moving the left block down
def block_left_down():
    y = block_left.ycor()
    y = y - 25
    block_left.sety(y)
# Moving the right block up
def block_right_up():
    y = block_right.ycor()
    y = y + 25
    block_right.sety(y)
# Moving right block down
def block_right_down():
    y = block_right.ycor()
    y = y - 25
    block_right.sety(y)
# Keyboard binding
a.listen()
a.onkeypress(block_left_up,"w")
a.onkeypress(block_left_down,"s")
a.onkeypress(block_right_up,"Up")
a.onkeypress(block_right_down,"Down")
# Main Game Loop
while True:
    a.update() # This is used to run any game
    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    # setting up the border
    if ball.ycor() > 290:   # Right top block Border
        ball.sety(290)
        ball_dy = ball_dy * -1
    if ball.ycor() < -290:  # Left top block Border
        ball.sety(-290)
        ball_dy = ball_dy * -1
    if ball.xcor() > 390:   # right width block Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=("Comic Sans MS'",24,"normal"))
    if(ball.xcor()) < -390: # Left width block Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=("Comic Sans MS",24,"normal"))
    # Handling the collisions with block.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < block_right.ycor() + 60 and ball.ycor() > block_right.ycor() - 60):
        ball.setx(340)
        ball_dx = ball_dx * -1
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < block_left.ycor() + 60 and ball.ycor() > block_left.ycor() - 60):
        ball.setx(-340)
        ball_dx = ball_dx * -1
    # Block Border
    y1=block_right.ycor()
    y=block_left.ycor()
    if block_right.ycor() >290:   # right block boarder up
        y1 = y1 - 60
        block_right.sety(y1)
    if block_right.ycor() <-290:    #right block boarder down
        y1 = y1 + 60
        block_right.sety(y1)
    if block_left.ycor()> 290:     # left block boarder down
        y = y - 60
        block_left.sety(y)
    if block_left.ycor() <-290:   # left block boarder up
        y = y + 60
        block_left.sety(y)
    # Winner
    if (player_a_score==5):
        x = "A"
        a.clear()
        break
    if (player_b_score==5):
        x = "B"
        a.clear()
        break
a.bgcolor("black")
a.setup(width=800,height=600)
pen.up()
pen.goto(-200,-15)
pen.down()
pen.write("Player {} is the WINNER!!!".format(x),font=('Comic Sans MS',24,"normal"))


                                                                        