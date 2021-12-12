import turtle

wn = turtle.Screen()
wn.title("PongGame By IamCat")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 100)
pen.write("PLAY", align="center", font=("Courier", 50, "normal"))

button = turtle.Turtle()
button.speed(0)
button.color("white")
button.penup()
button.hideturtle()
button.goto(0, 50)
button.write("press UP to play game", align="center", font=("Courier", 12, "normal"))


def buttongone():
    pen.clear()
    button.clear()
    import main


wn.listen()
wn.onkeypress(buttongone, "Up")

box = turtle.Turtle()
box.shape("square")
box.shapesize(2, 15)
box.color("black")
box.goto(0, 50)
box.dx = 2

while True:

    box.setx(box.xcor() + box.dx)

    if box.xcor() > 390:
        box.goto(-390, 50)

    wn.update()
