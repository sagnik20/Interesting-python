'''
A spiral web with turtle vector
Demo vecotr drawing
'''
import turtle
import time

pointer = turtle.Turtle()
pointer.shape('turtle')

s=10
pointer.speed(50)
# pointer.penup()
for i in range(60):
        s=s+2
        pointer.stamp()
        pointer.forward(s)
        pointer.right(45)
        time.sleep(0.20)
