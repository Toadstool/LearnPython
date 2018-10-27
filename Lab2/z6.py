import turtle
import sys
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
tess.color("blue")            # Tell tess to change her color
tess.pensize(3)               # Tell tess to set her pen width


while True:
   tess.forward(50+random.randint(0,10)-5)
   tess.left(120+random.randint(0,10)-5)
   tess.forward(50+random.randint(0,10)-5)


turtle.done()
