import turtle

color = ['red','purple','blue','green','yellow','orange']
turtle.bgcolor('black')

for s in range(360):
    turtle.pencolor(color[s%6])
    turtle.width(s/100+1)
    turtle.forward(s)
    turtle.left(59)