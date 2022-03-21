import turtle
turtle.begin_fill()
for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()
turtle.color('white')
turtle.penup()
turtle.goto(35, 25)
turtle.write('Hello', font=45)
def Button(x, y):
    if x in range(0, 100) and y in range(0, 50):
        .   .   .
turtle.onscreenclick(Button)
turtle.mainloop()