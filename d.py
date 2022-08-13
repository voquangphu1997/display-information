import turtle
t = turtle.Turtle()

# for background
screen = turtle.Screen()
screen.bgcolor("Blue")

#color and speed
# of turtle
t.color("black")
t.shape("turtle")
t.speed(10)

def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()
    
# base of the house
t.fillcolor('grey')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()

turtle.done()