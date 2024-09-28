import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Victoria Harbour")

# Setup the turtle
t = turtle.Turtle()
t.speed(10)  # Fastest drawing speed
# t.hideturtle()

# Function to draw a rectangle (for buildings)


def draw_building(width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw water (Victoria Harbour)


def draw_water():
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("deepskyblue")
    t.forward(800)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(200)
    t.end_fill()

# Draw the sky (background)


def draw_sky():
    t.penup()
    t.goto(-400, 150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("lightcyan")
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.end_fill()

# Draw mountains in the background


def draw_mountains():
    t.penup()
    t.goto(-400, 100)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    t.fillcolor("darkgreen")
    t.goto(-300, 200)
    t.goto(-200, 150)
    t.goto(-100, 200)
    t.goto(0, 150)
    t.goto(100, 200)
    t.goto(200, 150)
    t.goto(300, 200)
    t.goto(400, 100)
    t.goto(-400, 100)
    t.end_fill()

# Draw sun in the background


def drawFourRays(t, length, radius):

    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)


def draw_sun():
    t.penup()
    t.goto(85, 110)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()

    # Use the defined
    # function to draw rays
    t.penup()
    t.goto(85, 169)
    t.pendown()
    drawFourRays(t, 85, 54)
    t.right(45)
    drawFourRays(t, 85, 54)
    t.left(45)

# Draw windows on buildings


def draw_windows(x, t, width, height, rows, cols):
    t.penup()
    window_width = width / cols
    window_height = height / rows
    for row in range(rows):
        for col in range(cols):
            t.goto(x + col * window_width + 5, t + row * window_height + 5)
            t.pendown()
            t.begin_fill()
            t.fillcolor("lightyellow")
            for _ in range(2):
                t.forward(window_width - 10)
                t.left(90)
                t.forward(window_height - 10)
                t.left(90)
            t.end_fill()
            t.penup()

# Draw an abstract skyline


def draw_skyline():
    buildings = [
        (-350, -150, 60, 250, "gray", 5, 3),  # ICC Tower
        (-250, -150, 80, 200, "darkgray", 5, 4),  # Generic building
        (-150, -150, 60, 180, "dimgray", 5, 3),  # Another building
        (-50, -150, 40, 220, "darkslategray", 6, 2),  # Tall building
        (50, -150, 60, 300, "gray", 6, 3),  # Bank of China Tower
        (150, -150, 100, 180, "darkgray", 4, 4),  # Another building
        (250, -150, 90, 220, "dimgray", 5, 3)  # Another tall building
    ]

    # Draw buildings
    for building in buildings:
        x, t, width, height, color, rows, cols = building
        t.penup()
        t.goto(x, t)
        t.pendown()
        draw_building(width, height, color)
        draw_windows(x, t, width, height, rows, cols)

# Draw reflections in water


def draw_reflection():
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.setheading(0)
    t.color("lightblue")

    for _ in range(50):
        t.forward(8)
        t.penup()
        t.forward(8)
        t.pendown()
        t.forward(8)
        t.penup()
        t.forward(8)

# Draw the entire scene


# Set a timer to limit drawing to 60 seconds
start_time = time.time()
draw_sky()
draw_mountains()
draw_water()
# draw_skyline()
# draw_reflection()
end_time = time.time()

# Ensure the drawing is completed within 60 seconds
elapsed_time = end_time - start_time
if elapsed_time < 60:
    time.sleep(60 - elapsed_time)

# # Hide the turtle and display the window
turtle.done()
