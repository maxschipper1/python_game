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

print("he")

while True:
    wn.update()
    wn.listen()
    wn.onkeypress(player_right, "Right")
    wn.onkeypress(player_left, "Left")
    