import turtle 

wn = turtle.Screen()
wn.title("Game")
wn.setup(800, 600)
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.sety(-200)
player.setx(0)
player.color("white")
player.penup()

def player_right ():
    new_pos =  player.xcor() + 10
    player.setx(new_pos)

def player_left():
    new_pos = player.xcor() - 10
    player.setx(new_pos)


def create_bullet ():
    shot = turtle.Turtle()
    shot.shape("square")
    shot.penup()
    shot.speed(0)
    shot.shapesize(0.5)
    shot.color("white")
    return shot

def bullet_pos():
    print(player.xcor())
    create_bullet().setx(player.xcor())
    create_bullet().sety(100)
    
    

print("he")





while True:
    wn.update()
    wn.listen()
    wn.onkeypress(player_right, "Right")
    wn.onkeypress(player_left, "Left")
    wn.onkeypress(bullet_pos, "Up")

    if player.xcor() < -390:
        player.setx(-390)

    if player.xcor() > 390:
        player.setx(390)
    


    