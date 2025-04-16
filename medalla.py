import turtle
tia = turtle.Turtle()
tia.color("black")
tia.pensize(5)

#Escogemos un relleno e indicamos hasta donde rellenara con ese color
tia.fillcolor("blue")
tia.begin_fill()
tia.forward(160)    
tia.right(135)
tia.forward(100)
tia.right(45)
tia.forward(160)
tia.right(135)
tia.forward(100)
tia.end_fill() 

tia.fillcolor("green")
tia.begin_fill()
tia.left(90)
tia.forward(100)
tia.right(135)
tia.forward(160)
tia.right(45)
tia.forward(100)
tia.end_fill() 

turtle.done()