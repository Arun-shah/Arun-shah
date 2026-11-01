import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("#160d24")
screen.title("Happy Birthday ❤️")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Birthday person's name
name = "Diya"

if not name:
    name = "My Love"


# Rectangle drawing function
def rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


# Text function
def write_text(x, y, text, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(
        text,
        align="center",
        font=("Arial", size, "bold")
    )


# Plate
rectangle(-180, -190, 360, 15, "#eeeeee")
screen.update()
time.sleep(0.5)

# Bottom cake layer
rectangle(-150, -175, 300, 90, "#e57373")
screen.update()
time.sleep(0.7)

# Bottom frosting
rectangle(-150, -95, 300, 12, "#fff0f5")
screen.update()
time.sleep(0.5)

# Middle cake layer
rectangle(-120, -83, 240, 75, "#ffb74d")
screen.update()
time.sleep(0.7)

# Middle frosting
rectangle(-120, -15, 240, 12, "#ffffff")
screen.update()
time.sleep(0.5)

# Top cake layer
rectangle(-85, -3, 170, 65, "#f06292")
screen.update()
time.sleep(0.7)

# Top frosting
rectangle(-85, 52, 170, 12, "#fff0f5")
screen.update()
time.sleep(0.5)


# Cake decorations
for x in range(-125, 126, 25):
    pen.penup()
    pen.goto(x, -135)
    pen.dot(9, "#ffeb3b")

for x in range(-95, 96, 25):
    pen.penup()
    pen.goto(x, -45)
    pen.dot(8, "#ffffff")

screen.update()
time.sleep(0.5)


# Candles
for x in [-40, 0, 40]:
    rectangle(x - 5, 64, 10, 45, "#80deea")
    screen.update()
    time.sleep(0.4)

    # Candle flame
    pen.penup()
    pen.goto(x, 115)
    pen.dot(17, "#ff9800")
    pen.goto(x, 118)
    pen.dot(8, "#ffeb3b")

screen.update()
time.sleep(0.5)


# Birthday message
write_text(0, -260, "Happy Birthday!", 28, "#ff80ab")
screen.update()
time.sleep(0.5)

write_text(0, -300, name, 25, "#ffd54f")
screen.update()

# Decorative stars
for _ in range(35):
    x = random.randint(-370, 370)
    y = random.randint(-330, 330)

    pen.penup()
    pen.goto(x, y)
    pen.dot(random.randint(2, 5), "#ffffff")

screen.update()

# Final message
write_text(
    0, 220,
    "✨ A Special Day For You ✨\nBy Sanjiwan",
    18, "#ffffff"
)
screen.update()

turtle.done()
