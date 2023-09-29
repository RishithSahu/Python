import turtle
turtle.setup(800,600)
window = turtle.Screen()
window.title("My Polygon")
jfjf = turtle.getturtle()
turtle.register_shape("poly1",((0,0),(100,0),(140,40)))
jfjf.shape("poly1")
jfjf.fillcolor("white")
jfjf.setposition(100,0)

window.exitonclick()