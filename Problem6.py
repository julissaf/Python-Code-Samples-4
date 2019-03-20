#Julissa Franco
#02.28.2019
# Problem 6


import turtle

def drawSquare(t, sz):
    for i in range(5):
        t.forward(sz)
        t.left(108)
     
wn= turtle.Screen()

alex=turtle.Turtle()
alex.color("red")


size= [30, 60, 90, 120, 150]

for x in size:
    drawSquare(alex, x)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

#drawSquare(alex, 100)


wn.exitonclick()
