import turtle
t = turtle.Turtle()
t.speed(90)
colors = ['red','blue','green','yellow','purple','cornflowerblue','aquamarine','orange']
for i in colors:
  t.pencolor(i)
  for i in range(4):
    t.fd(25)
    t.rt(90)
  t.rt(45)