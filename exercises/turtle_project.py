"""This scene portrays the planet Mars and the day we colonize the planet to make a second home for humanity.

Line 124-128 demonstrates "breaking up complex functions" as the once complex draw_rocketship function now contains 3

simpler functions. I also attempted to go "above and beyond" by using the t.screen.bgcolor function in line 19,

which sets the background color to the color of your choice. Additionally, I used the write function in line 28 to add text to your screen.

"""
 
__author__ = "730672573"
 
from turtle import Turtle, colormode, done

colormode(255)

 
def main() -> None:
    """The entrypoint of my scene."""
    tesla: Turtle = Turtle()
    tesla.speed(100)
    tesla.screen.bgcolor("black")
    draw_circle(tesla, 10, 0, 100, "orange")
    draw_circle(tesla, -300, 220, 50, "yellow")
    draw_star(tesla, -50, -50, 30)
    draw_rocketship(tesla, 10, 300)
    tesla.penup()
    tesla.goto(-150, -300)  # Adjust the coordinates to position the text
    tesla.pendown()
    tesla.color("white")  # Text color
    tesla.write("OCCUPY \n MARS", font=("Arial", 60, "normal"))
    draw_star(tesla, -150, -40, 30)
    draw_star(tesla, -300, -30, 30)
    draw_star(tesla, -300, -300, 30)
    draw_star(tesla, -330, -220, 30)
    draw_star(tesla, -270, -180, 30)
    draw_star(tesla, 300, -300, 30)
    draw_star(tesla, 330, -220, 30)
    draw_star(tesla, 270, -180, 30)
    draw_star(tesla, 300, 300, 30)
    draw_star(tesla, 330, 220, 30)
    draw_star(tesla, 270, 180, 30)
    draw_star(tesla, 300, 100, 30)
    draw_star(tesla, 330, 50, 30)
    draw_star(tesla, 270, 0, 30)
    draw_star(tesla, 80, -50, 30)
    draw_star(tesla, -300, 140, 30)
    draw_star(tesla, -230, 100, 30)
    draw_star(tesla, -200, 300, 30)
    draw_star(tesla, 150, 250, 30)
    done()


def draw_circle(t: Turtle, x: float, y: float, radius: float, color: str) -> None:
    """Draw a filled circle at the specified coordinates (x, y) with the given radius and color."""
    t.color(color, color)
    t.speed(50)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_star(t: Turtle, x: float, y: float, size: int) -> None:
    """Draw a 5-pointed star at the specified coordinates (x, y) with the given size."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(1000)  # Set drawing speed (adjust as needed)

    t.fillcolor("yellow")  # Fill the star with a color
    t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()


def draw_triangle(t: Turtle, x: float, y: float, side_length: int, color: str) -> None:
    """Draw a 3 sided Triangle at the specified coordinates (x, y) with the given size and color."""
    t.color(color, color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    i: int = 0
    while (i < 3):
        t.forward(side_length)
        t.left(120)
        i = i + 1
    t.end_fill()


def draw_rectangle(t: Turtle, x: float, y: float, length: float, height: float, color: str) -> None:
    """Draw a rectangle at the specified coordinates (x, y) with the given legnth, hieght and color."""
    t.color(color, color)
    t.speed(50)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    i: int = 0
    while i < 2:
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
        i = i + 1
    t.end_fill()


def draw_fire(t: Turtle, x: float, y: float, side_length: int, color: str) -> None:
    """Draw fuel coming out of the rocket at the specified coordinates (x, y) with the given side length and color."""
    t.color(color, color)
    t.penup()
    t.goto(x + 5, y)
    t.pendown()
    t.begin_fill()
    i: int = 0
    while (i < 3):
        t.forward(side_length)
        t.right(120)
        i = i + 1
    t.end_fill()


def draw_rocketship(t: Turtle, x: float, y: float) -> None:
    """Draw a rocketship at the specified coordinates (x, y)."""
    draw_rectangle(t, x, y, 20, 50, "gray")
    draw_triangle(t, x, y, 20, "gray")
    draw_fire(t, x + 1, y - 50, 10, "yellow")


if __name__ == "__main__":
    main()