import time
import turtle
from turtle import *
import keyboard

turtle.register_shape("background.gif")
custom = False
game = False
wn = Screen()
wn.title("Space Battle")
wn.tracer(0)
wn.setup(1200, 768)
wn.bgpic("background.gif")
penp = Turtle()
penp.speed(0)
penp.shape("square")
penp.color("white")
penp.penup()
penp.hideturtle()
penp.goto(0, 0)
penp.write(f"Press p to Start", align="center", font=("Courier", 15, "normal"))
penc = Turtle()
penc.speed(0)
penc.shape("square")
penc.color("white")
penc.penup()
penc.hideturtle()
penc.goto(0, -30)
penc.write(f"Press Shift to Change controls", align="center", font=("Courier", 15, "normal"))
# Screen
start = True

while start:
    if keyboard.is_pressed("p"):
        game = True
        start = False
    if keyboard.is_pressed("Shift"):
        custom = True

        keynorm1 = wn.textinput(title="Keybinds for normal Attack of Player 1", prompt="Type the Key")
        keyp1 = wn.textinput(title="Keybinds for Power Attack of Player 1", prompt="Type the Key")
        keynorm2 = wn.textinput(title="Keybinds for normal Attack of Player 2", prompt="Type the Key")
        keyp2 = wn.textinput(title="Keybinds for Power Attack of Player 2", prompt="Type the Key")
        if keynorm1 == "":
            keynorm1 = "k"
        if keyp2 == "":
            keyp2 = "2"
        if keyp1 == "":
            keyp1 = "l"
        if keynorm2 == "":
            keynorm2 = "1"

turtle.register_shape('destroyer.gif')
turtle.register_shape('destroyer2.gif')
turtle.register_shape('bulletk.gif')
turtle.register_shape('bulletl.gif')
turtle.register_shape('bullet1.gif')
turtle.register_shape('bullet2.gif')
penc.clear()
penp.clear()
# Player 1
p1 = Turtle()
p1.speed(0)
p1.shape("destroyer2.gif")
p1.color("red")
p1.penup()
p1.goto(0, -300)
p1.direction = "stop"

p = p1.xcor()
q = p1.ycor()
health1 = 100
health2 = 100

# player 1 bulletK

bulletk = Turtle()
bulletk.speed(0)
bulletk.shape("bulletk.gif")
bulletk.color("white")
bulletk.penup()
bulletk.goto(p, q)
bulletk.direction = "stop"
bulletk.shapesize(0.8, 0.8)
bulletk.setheading(90)
bulletk.hideturtle()
bulletk_speed = 2
bulletk_state = 'ready'

# bulletl player 1

bulletl = Turtle()
bulletl.speed(0)
bulletl.shape("bulletl.gif")
bulletl.color("red")
bulletl.penup()
bulletl.goto(p, q)
bulletl.direction = "stop"
bulletl.setheading(90)
bulletl.hideturtle()
bulletl_speed = 2
bulletl_state = 'ready'
# Player 2
p2 = Turtle()
p2.speed(0)
p2.shape("destroyer.gif")
p2.color("blue")
p2.penup()
p2.goto(0, 300)
p2.direction = "stop"

P = p2.xcor()
Q = p2.ycor()

# player 2 bullet1

bullet1 = Turtle()
bullet1.speed(0)
bullet1.shape("bullet1.gif")
bullet1.color("white")
bullet1.penup()
bullet1.goto(P, Q)
bullet1.direction = "stop"
bullet1.shapesize(0.8, 0.8)
bullet1.setheading(270)
bullet1.hideturtle()
bullet1_speed = 2
bullet1_state = 'ready'

# bullet2 player 2
ammo1 = 50
ammo2 = 50

bullet2 = Turtle()
bullet2.speed(0)
bullet2.shape("bullet2.gif")
bullet2.color("red")
bullet2.penup()
bullet2.goto(P, Q)
bullet2.direction = "stop"
bullet2.setheading(270)
bullet2.hideturtle()
bullet2_speed = 2
bullet2_state = 'ready'

pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(520, 330)
pen.write(f"Health:{health2}", align="center", font=("Courier", 15, "normal"))

pen2 = Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(520, -330)
pen2.write(f"Health:{health1}", align="center", font=("Courier", 15, "normal"))

pen3 = Turtle()
pen3.speed(0)
pen3.shape("square")
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, 0)

pena1 = Turtle()
pena1.speed(0)
pena1.shape("square")
pena1.color("white")
pena1.penup()
pena1.hideturtle()
pena1.goto(340, -330)
pena1.write(f"Powered ammo:{ammo1}", align="center", font=("Courier", 15, "normal"))

pena2 = Turtle()
pena2.speed(0)
pena2.shape("square")
pena2.color("white")
pena2.penup()
pena2.hideturtle()
pena2.goto(340, 330)
pena2.write(f"Powered ammo:{ammo2}", align="center", font=("Courier", 15, "normal"))


# Movement_Of_Players

def move1():
    if keyboard.is_pressed("Right") and p1.xcor() < 550:
        x = p1.xcor()
        p1.setx(x + 0.8)
        p1.direction = "stop"
    if keyboard.is_pressed("Left") and p1.xcor() > -550:
        x = p1.xcor()
        p1.setx(x - 0.8)
    if bulletk.direction == "up":
        a = bulletk.ycor()
        bulletk.sety(a + 1)
    if bulletl.direction == "up":
        a = bulletl.ycor()
        bulletl.sety(a + 1)


def move2():
    if keyboard.is_pressed("d") and p2.xcor() < 550:
        x = p2.xcor()
        p2.setx(x + 0.8)
    if keyboard.is_pressed("a") and p2.xcor() > -550:
        x = p2.xcor()
        p2.setx(x - 0.8)
    if bullet1.direction == "down":
        a = bullet1.ycor()
        bullet1.sety(a - 1)
    if bullet2.direction == "down":
        a = bullet2.ycor()
        bullet2.sety(a - 1)


def fire_k():
    global bulletk_state

    if bulletk_state == "ready":
        bulletk_state = "fire"

        x = p1.xcor()
        y = p1.ycor() + 10
        bulletk.goto(x, y)
        bulletk.showturtle()


def fire_l():
    global bulletl_state
    global ammo1
    if bulletl_state == "ready" and ammo1 > 0:
        bulletl_state = "fire"
        ammo1 -= 1
        pena1.clear()
        pena1.write(f"Powered ammo:{ammo1}", align="center", font=("Courier", 15, "normal"))
        x = p1.xcor()
        y = p1.ycor() + 10
        bulletl.goto(x, y)
        bulletl.showturtle()


def fire_2():
    global bullet2_state
    global ammo2
    if bullet2_state == "ready" and ammo2 > 0:
        bullet2_state = "fire"
        ammo2 -= 1
        pena2.clear()
        pena2.write(f"Powered ammo:{ammo2}", align="center", font=("Courier", 15, "normal"))
        x = p2.xcor()
        y = p2.ycor() - 10
        bullet2.goto(x, y)
        bullet2.showturtle()


def fire_1():
    global bullet1_state

    if bullet1_state == "ready":
        bullet1_state = "fire"

        x = p2.xcor()
        y = p2.ycor() - 10
        bullet1.goto(x, y)
        bullet1.showturtle()


def IsCollision(a, b):
    Distance = (((a.xcor() - b.xcor()) ** 2) + ((a.ycor() - b.ycor()) ** 2) ** 0.5)
    if Distance < 45:
        return True
    else:
        return False


# Controls
wn.listen()
if custom:
    wn.onkeypress(fun=fire_k, key=keynorm1)
    wn.onkeypress(fun=fire_l, key=keyp1)
    wn.onkeypress(fun=fire_2, key=keyp2)
    wn.onkeypress(fun=fire_1, key=keynorm2)
else:
    wn.onkeypress(fun=fire_k, key="k")
    wn.onkeypress(fun=fire_l, key="l")
    wn.onkeypress(fun=fire_2, key="2")
    wn.onkeypress(fun=fire_1, key="1")
bulletl_collision = False
bullet2_collision = False
while True:
    wn.update()
    move1()
    move2()
    if bulletk_state == "fire":
        y = bulletk.ycor()
        y += bulletk_speed
        bulletk.sety(y)

    if bulletk.ycor() > 330:
        bulletk.hideturtle()
        bulletk_state = "ready"

    if bulletl_state == "fire" and ammo1 > -1:
        y = bulletl.ycor()
        y += bulletl_speed
        bulletl.sety(y)

    if bulletl.ycor() > 330:
        bulletl.hideturtle()
        bulletl_state = "ready"

    if bullet1_state == "fire":
        y = bullet1.ycor()
        y -= bullet1_speed
        bullet1.sety(y)
    if bullet1.ycor() < -330:
        bullet1.hideturtle()
        bullet1_state = "ready"

    if bullet2_state == "fire" and ammo2 > -1:
        y = bullet2.ycor()
        y -= bullet2_speed
        bullet2.sety(y)

    if bullet2.ycor() < -330:
        bullet2.hideturtle()
        bullet2_state = "ready"

    if IsCollision(bulletk, p2):
        bulletk.hideturtle()
        bulletk_state = "ready"
        bulletk.goto(0, -400)
        health2 -= 10
        pen.clear()
        pen.write(f"Health:{health2}", align="center", font=("Courier", 15, "normal"))
    if IsCollision(bulletl, p2):
        bulletl.hideturtle()
        bulletl_state = "ready"
        bulletl.goto(0, -400)
        if bulletl_collision:
            health2 -= 5
            bulletl_collision = False
        else:
            health2 -= 15
        pen.clear()
        pen.write(f"Health:{health2}", align="center", font=("Courier", 15, "normal"))
    if IsCollision(bullet1, p1):
        bullet1.hideturtle()
        bullet1_state = "ready"
        bullet1.goto(0, 400)
        health1 -= 10
        pen2.clear()
        pen2.write(f"Health:{health1}", align="center", font=("Courier", 15, "normal"))
    if IsCollision(bullet2, p1):
        bullet2.hideturtle()
        bullet2_state = "ready"
        bullet2.goto(0, 400)
        if bullet2_collision:
            health1 -= 5
            bullet2_collision = False
        else:
            health1 -= 15
        pen2.clear()
        pen2.write(f"Health:{health1}", align="center", font=("Courier", 15, "normal"))

    if health1 <= 0:
        pen3.write("Player 2 Wins", align='center', font=("Courier", 40, "normal"))
        time.sleep(3)
        break
    if health2 <= 0:
        pen3.write("Player 1 Wins", align='center', font=("Courier", 40, "normal"))
        time.sleep(3)
        break
    if IsCollision(bulletk, bullet1):
        bullet1.hideturtle()
        bullet1_state = "ready"
        bullet1.goto(0, 400)
        bulletk.hideturtle()
        bulletk_state = "ready"
        bulletk.goto(0, -400)
    if IsCollision(bullet2, bulletl):
        bulletl.hideturtle()
        bulletl_state = "ready"
        bulletl.goto(0, -400)
        bullet2.hideturtle()
        bullet2_state = "ready"
        bullet2.goto(0, 400)
    if IsCollision(bulletk, bullet2):
        bulletk.hideturtle()
        bulletk_state = "ready"
        bulletk.goto(0, -400)
        bullet2_collision = True
    if IsCollision(bulletl, bullet1):
        bullet1.hideturtle()
        bullet1_state = "ready"
        bullet1.goto(0, 400)
        bulletl_collision = True
