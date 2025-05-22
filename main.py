import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)

def draw_equilateral_triangle():
    pen.color("black", "yellow")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()

def draw_rectangle():
    pen.color("black", "green")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(150)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
    pen.end_fill()

def draw_hexagon():
    pen.color("black", "orange")
    pen.begin_fill()
    for _ in range(6):
        pen.forward(70)
        pen.left(60)
    pen.end_fill()

pen.penup()
pen.goto(-200, 100)
pen.pendown()
draw_equilateral_triangle()

pen.penup()
pen.goto(50, 100)
pen.pendown()
draw_rectangle()

pen.penup()
pen.goto(-75, -100)
pen.pendown()
draw_hexagon()

pen.hideturtle()
screen.mainloop()
