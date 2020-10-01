from turtle import *    # importing all the library from turtle

color('green','yellow')   #specifying color
begin_fill()

while True:    # while the condition is true the loop will run
    forward(200)   # command for making it move forward
    left(170)   # to move left
    if abs(pos()) < 1 :  # checking absolute value
        break

end_fill()
done()
