#Julissa Franco
#02.28.2019
#Use chunk of code to produce an image


import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
     
wn= turtle.Screen()

alex=turtle.Turtle()
alex.color("blue")

size= [20, 40, 60, 80, 100]

for x in size:
    drawSquare(alex, x)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

#drawSquare(alex, 50)


#drawSquare(alex, 100)


#drawSquare(alex, 150)

wn.exitonclick()
