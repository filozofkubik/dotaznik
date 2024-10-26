import turtle
import random
turtle.Screen().colormode(255)
pencil = turtle.Turtle()
pencil.shape("circle")
text =["pravice", "libertariánství", "levice", "autoritářství"]
for i in range (4):
    pencil.forward(400)
    pencil.write(text[i])
    pencil.backward(400)
    pencil.right(90)

turtle.done()

answer = int(input("kterou odpov2d?????"))
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
q9 = []
q10 = []
#pokus 1