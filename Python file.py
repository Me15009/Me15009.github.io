import turtle
t = turtle.pen()
turtle.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray","pink","brown",
"lime","cyan","violet","olive","navy","maroon","yellow green","silver","gold","tan"]
sides = int( turtle.numinput("Number of sides",
                             "How many sides do you want(1-20)?", 4, 1, 20))
for x in range(360):
    turtle.pencolor( colors[x % sides] )
    turtle.forward( x * 3 / sides + x)
    turtle.left(360 / sides + 1)
    turtle.width(x * sides / 200)
