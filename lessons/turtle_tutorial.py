from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
i: int = 0
leo.penup()
leo.goto(-140, -60)
leo.pendown()
leo.color(246, 127, 17)
leo.begin_fill()
leo.speed(50)
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0,0,0)
bob.penup()
bob.goto(-140, -60)
bob.pendown()
bob.speed(100)
side_length: int = 300 * 0.97
while i < 1000:
    bob.forward(side_length)
    bob.left(121)
    i += 1
done()