import turtle

window = turtle.Screen()
window.title("Absolute Positioning")

turt =  turtle.getturtle()
turt.hideturtle()
turt.setposition(100,0)
turt.setposition(100,100)
turt.setposition(0,100)
turt.setposition(0,0)
window.exitonclick()