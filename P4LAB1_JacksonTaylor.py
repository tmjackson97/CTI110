import turtle

win = turtle.Screen()
win.bgcolor("lightblue")

t = turtle.Turtle()
t.color("green") 
t.pensize(2)
t.speed(3)

t.penup()
t.goto(-50, -50) 
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50, 50) 
t.pendown()

t.fillcolor("green")
t.begin_fill()

sides_drawn = 0
while sides_drawn < 3:
    t.forward(100)
    t.left(120)
    sides_drawn += 1

t.end_fill()

t.hideturtle()
win.mainloop()