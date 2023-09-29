import turtle

window = turtle.Screen()
window.title("Absolute Positioning")

turt =  turtle.getturtle()
turt.showturtle()
turt.pensize(2)
turtle.colormode(255)
turt.pencolor(238,130,238)
turt.setposition(100,0)
turt.setposition(100,100)
turt.setposition(0,100)
turt.setposition(0,0)
turt.setposition(0,-100)
turt.setposition(100,-100)
turt.setposition(100,0)
turt.setposition(0,0)

window.exitonclick()
# Window.exitonclick() must always be at the end of the program.