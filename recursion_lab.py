'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor("sky blue")
color_list = ["white","violet","steelblue4","dark slate blue","darkseagreen4", "dark olive green", "dark green"]

def draw(my_turtle,x,y, heading, dist, depth):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.color(color_list[depth%len(color_list)])
    my_turtle.down()
    my_turtle.setheading(heading)
    my_turtle.forward(dist)

    new_y = my_turtle.ycor()
    new_x = my_turtle.xcor()
    if depth > 0:
        draw(my_turtle, new_x,new_y, heading +40, dist/1.7, depth - 1)
        draw(my_turtle, new_x, new_y, heading -40, dist/1.7, depth - 1)

my_turtle.speed(0)
my_turtle.width(3)
for i in range(0,360, 90):
    draw(my_turtle, 0,0,i,100,6)

my_screen.exitonclick()