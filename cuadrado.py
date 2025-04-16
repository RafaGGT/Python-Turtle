import turtle
tia = turtle.Turtle()
# Dejamos de dibujar, cambiamos a la cordenada y volvermos a colocar el lapiz para dibujar
tia.penup()
tia.goto(-160, 160)
tia.pendown()
# Color del rastro de la tortuga
tia.color("black")   
tia.right(90)  
tia.forward(320)    
tia.left(90)  
tia.forward(320)   
tia.left(90)  
tia.forward(320)   
tia.left(90)  
tia.forward(320)   
#Mantenemos la ventana abierta
turtle.done()