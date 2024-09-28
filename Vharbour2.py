import turtle as t

# Setup the screen
t.speed(3)
t.bgcolor("lightblue")
t.title("Pandas")


def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# Draw face
def draw_face():
    draw_circle("white", 100, 0, -100)

# Draw eyes


def draw_eyes():
    draw_circle("black", 15, -35, -30)  # Left eye
    draw_circle("black", 15, 35, -30)   # Right eye
    draw_circle("white", 7, -35, -25)   # Left eye ball
    draw_circle("white", 7, 35, -25)    # Right eye ball

# Draw nose


def draw_nose():
    draw_circle("black", 10, 0, -50)
    draw_circle("white", 5, 0, -53)     # Nose highlight


# Draw mouth
def draw_mouth():
    t.penup()
    t.goto(-10, -60)
    t.pendown()
    t.setheading(-60)  # Angle for the mouth
    t.circle(10, 120)  # Draw a semicircle for the mouth

# Draw ears


def draw_ears():
    draw_circle("black", 40, 120, 0)  # Left ear
    draw_circle("black", 40, -120, 0)   # Right ear


# Start drawing
draw_face()
draw_ears()
draw_eyes()
draw_nose()
draw_mouth()

t.hideturtle()
t.done()
