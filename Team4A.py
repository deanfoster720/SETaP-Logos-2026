import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Helper function to draw a filled circle
def filled_circle(radius, fill_color, outline_color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw coin
filled_circle(120, "#f2a900", "#d18b00")
filled_circle(105, "#ffd700", "#ffd700")

t.pensize(12)

t.color("#8b5a00")

t.penup()
t.goto(20, 45)   # offset to the right & slightly down
t.pendown()

# Vertical bar
t.setheading(-90)
t.forward(100)

# Bottom bar
t.setheading(0)
t.forward(45)

# ---- Draw E (FRONT) ----
t.color("black")

t.penup()
t.goto(-55, 50)
t.pendown()

# Vertical bar
t.setheading(-90)
t.forward(100)

# Top bar
t.penup()
t.goto(-55, 50)
t.pendown()
t.setheading(0)
t.forward(40)

# Middle bar
t.penup()
t.goto(-55, 0)
t.pendown()
t.forward(30)

# Bottom bar
t.penup()
t.goto(-55, -50)
t.pendown()
t.forward(40)

turtle.done()
