from turtle import *

#paint a house
speed(30)
#drowing a square

width(6)

color("purple")
forward (200)

left(90)
forward(200)

left(90)
forward(200)
left(90)
forward(200)
#end of a square

#drawing a door

left(90)
forward(70)

color("black")
begin_fill()
left(90)
forward(120)     #height of the door

right(90)
forward(60)

right(90)
forward(120)
end_fill()
#end of the door

#drawing a roof
penup()
goto(200, 200)

color("orange")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

penup()
goto(200, 200)
pendown()

right(120)
forward(200)
left(120)
forward(200)

penup()
# drawing a window

color("blue")

begin_fill()
goto(30, 180)
left(30)
pendown()

begin_fill()

forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)

end_fill()

penup()
goto(170, 180)
pendown()

begin_fill()

forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)

end_fill()


exitonclick()

