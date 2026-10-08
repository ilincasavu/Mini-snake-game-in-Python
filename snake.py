import turtle
import random
import time

# Settings 
STEP = 20          # size of one grid square
LIMIT = 280        # how far the snake can go before hitting a wall
DELAY_MS = 100     # lower = faster game

score = 0
high_score = 0

# Screen
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # we redraw manually, which makes movement smooth

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Body segments           
segments = []

# Score display           
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 260)


def update_score():
    pen.clear()
    pen.write(f"Score: {score}   High Score: {high_score}",
              align="center", font=("Courier", 18, "normal"))


# Controls           
# We block 180 degree turns so the snake can't reverse into itself.
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


# Game logic           
def move_head():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + STEP)
    elif head.direction == "down":
        head.sety(y   STEP)
    elif head.direction == "left":
        head.setx(x   STEP)
    elif head.direction == "right":
        head.setx(x + STEP)


def game_over():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # hide the old body segments offscreen, then forget them
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    update_score()


def game_loop():
    global score, high_score

    # Hit a wall?
    if abs(head.xcor()) > LIMIT or abs(head.ycor()) > LIMIT:
        game_over()

    # Ate the food?
    if head.distance(food) < 20:
        # place food on a random grid square
        x = random.randrange( LIMIT, LIMIT + 1, STEP)
        y = random.randrange( LIMIT, LIMIT + 1, STEP)
        food.goto(x, y)

        # grow the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move each segment to where the one in front of it was (back to front)
    for i in range(len(segments)   1, 0,  1):
        segments[i].goto(segments[i   1].position())
    if segments:
        segments[0].goto(head.position())

    move_head()

    # Hit yourself?
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()
            break

    screen.update()
    screen.ontimer(game_loop, DELAY_MS)  # run again after a short delay


update_score()
game_loop()
screen.mainloop()
