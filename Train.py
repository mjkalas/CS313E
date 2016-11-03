#  File: Train.py
#  Description: This program draws a train using Turtle Graphics
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 313E
#  Unique Number: 50945
#  Date Created: 02/22/16
#  Date Last Modified: 02/29/16

import turtle

def drawSquare (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0) # set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.penup()

def main ():
  # put label on top of page
  turtle.title ('Train')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  #draw railroad tracks
  ttl.pensize(2)
  ttl.penup()
  ttl.goto(-400, -175)
  ttl.pendown()
  ttl.goto(400, -175)
  ttl.penup()

  ttl.goto(-400, -200)
  ttl.pendown()
  ttl.goto(400, -200)
  ttl.penup()

  x = -390
  y = -200
  for i in range (13):
    ttl.goto(x, y)
    ttl.pendown()
    ttl.goto(x, y-10)
    ttl.goto(x + 30, y-10)
    ttl.goto(x + 30, y)
    ttl.penup()
    x += 60

  ttl.pencolor('blue')
  ttl.goto(-350, -90) #arc 1 starts here
  ttl.pendown()
  ttl.goto(-380, -90)
  ttl.goto(-380, 175)
  ttl.goto(-220, 175)
  ttl.goto(-220, -90)
  ttl.penup()

  ttl.goto(-240, -90) #arc 1 ends here
  ttl.pendown()
  ttl.goto(-150, -90) #arc 2 starts here
  ttl.penup()

  ttl.goto(-350, 175)
  ttl.pendown()
  ttl.goto(-395, 175)
  ttl.goto(-395, 195)
  ttl.goto(-200, 195)
  ttl.goto(-200, 175)
  ttl.goto(-220, 175)
  ttl.penup()

  ttl.goto(-220, 105)
  ttl.pendown()
  ttl.goto(300, 105)
  ttl.goto(300, -125)
  ttl.goto(380, -125)
  ttl.goto(350, -75)
  ttl.goto(300, -75)
  ttl.penup()

  ttl.goto(300, -65)
  ttl.pendown()
  ttl.goto(320, -65)
  ttl.goto(320, 80)
  ttl.goto(300, 80)
  ttl.penup()

  ttl.goto(320, -40)
  ttl.pendown()
  ttl.goto(340, -40)
  ttl.goto(340, 50)
  ttl.goto(320, 50)
  ttl.penup()

  ttl.goto(300, 5)
  ttl.pendown()
  ttl.goto(-220, 5)
  ttl.goto(-220, 15)
  ttl.goto(300, 15)
  ttl.penup()

  ttl.goto(-220, 10)
  ttl.pencolor('black')
  for i in range (0, 58):
    ttl.pendown()
    ttl.dot()
    ttl.penup()
    ttl.forward(9)

  ttl.goto(195, 105)
  ttl.pencolor('blue')
  ttl.pendown()
  ttl.goto(225, 225)
  ttl.goto(125, 225)
  ttl.goto(155, 105)
  ttl.penup()

  ttl.goto(225, 225)
  ttl.pendown()
  ttl.goto(215, 245)
  ttl.goto(135, 245)
  ttl.goto(125, 225)
  ttl.penup()

  ttl.goto(70, 105)
  ttl.pendown()
  ttl.goto(70, 155)
  ttl.goto(10, 155)
  ttl.goto(10, 105)
  ttl.penup()

  ttl.goto(60, 155)
  ttl.pendown()
  ttl.goto(60, 175)
  ttl.goto(20, 175)
  ttl.goto(20, 155)
  ttl.penup()  

  ttl.goto(-10, 105)
  ttl.pendown()
  ttl.goto(-10, 15)
  ttl.goto(-20, 15)
  ttl.goto(-20, 105)
  ttl.penup()

  x = -15
  y = 20
  ttl.pencolor('black')
  for i in range (0, 11):
    ttl.goto(x, y)
    ttl.pendown()
    ttl.dot()
    ttl.penup()
    y += 8

  ttl.goto(170, 105)
  ttl.pendown()
  ttl.pencolor('blue')
  ttl.goto(170, 15)
  ttl.goto(180, 15)
  ttl.goto(180, 105)
  ttl.penup()

  x = 175
  y = 20
  ttl.pencolor('black')
  for i in range (0, 11):
    ttl.goto(x, y)
    ttl.pendown()
    ttl.dot()
    ttl.penup()
    y += 8

  ttl.goto(-15, -90) #arc 2 ends here
  ttl.pencolor('blue')
  ttl.pendown()
  ttl.goto(120, -90)
  ttl.penup()

  ttl.goto(240, -90) #arc 3 ends here
  ttl.pendown()
  ttl.goto(300, -90)
  ttl.penup()

  ttl.fillcolor('grey')
  ttl.begin_fill()
  drawSquare(ttl, -360, 125, 50)
  ttl.end_fill()

  ttl.fillcolor('grey')
  ttl.begin_fill()
  drawSquare(ttl, -300, 125, 50)
  ttl.end_fill()

  #wheels
  ttl.goto(-295, -130)
  ttl.pendown()
  ttl.pencolor('red')
  ttl.circle(10)
  ttl.penup()

  ttl.goto(-295, -165)
  ttl.pendown()
  ttl.circle(45)
  ttl.penup()

  ttl.goto(-295, -175)
  ttl.pendown()
  ttl.circle(55)
  ttl.penup()

  ttl.goto(-80, -140)
  ttl.pendown()
  ttl.circle(10)
  ttl.penup()

  ttl.goto(-80, -165)
  ttl.pendown()
  ttl.circle(40)
  ttl.penup()

  ttl.goto(-80, -175)
  ttl.pendown()
  ttl.circle(50)
  ttl.penup()

  ttl.goto(185, -140)
  ttl.pendown()
  ttl.circle(10)
  ttl.penup()

  ttl.goto(185, -165)
  ttl.pendown()
  ttl.circle(40)
  ttl.penup()

  ttl.goto(185, -175)
  ttl.pendown()
  ttl.circle(50)
  ttl.penup()

  #spokes wheel 3
  ttl.goto(183, -140)
  ttl.pendown()
  ttl.goto(180, -165)
  ttl.goto(190, -165)
  ttl.goto(187, -140)
  ttl.penup()

  ttl.goto(183, -120)
  ttl.pendown()
  ttl.goto(180, -85)
  ttl.goto(190, -85)
  ttl.goto(187, -120)
  ttl.penup()

  ttl.goto(175, -130)
  ttl.pendown()
  ttl.goto(145, -133)
  ttl.goto(145, -123)
  ttl.goto(175, -126)
  ttl.penup()

  ttl.goto(195, -130)
  ttl.pendown()
  ttl.goto(225, -133)
  ttl.goto(225, -123)
  ttl.goto(195, -126)
  ttl.penup()

  ttl.goto(190, -119)
  ttl.pendown()
  ttl.goto(210, -95)
  ttl.goto(220, -105)
  ttl.goto(193, -122)
  ttl.penup()

  ttl.goto(180, -139)
  ttl.pendown()
  ttl.goto(165, -158)
  ttl.goto(157, -153)
  ttl.goto(177, -133)
  ttl.penup()

  ttl.goto(163, -93)
  ttl.pendown()
  ttl.goto(179, -122)
  ttl.goto(175, -123)
  ttl.goto(154, -99)
  ttl.penup()

  ttl.goto(190, -139)
  ttl.pendown()
  ttl.goto(205, -160)
  ttl.goto(215, -153)
  ttl.goto(192, -135)
  ttl.penup()

  #spokes wheel 2
  ttl.goto(-82, -120)
  ttl.pendown()
  ttl.goto(-85, -85)
  ttl.goto(-75, -85)
  ttl.goto(-78, -120)
  ttl.penup()

  ttl.goto(-82, -140)
  ttl.pendown()
  ttl.goto(-85, -165)
  ttl.goto(-75, -165)
  ttl.goto(-78, -140)
  ttl.penup()

  ttl.goto(-90, -130)
  ttl.pendown()
  ttl.goto(-120, -133)
  ttl.goto(-120, -123)
  ttl.goto(-90, -126)
  ttl.penup()

  ttl.goto(-70, -130)
  ttl.pendown()
  ttl.goto(-40, -133)
  ttl.goto(-40, -123)
  ttl.goto(-70, -126)
  ttl.penup()

  ttl.goto(-75, -119)
  ttl.pendown()
  ttl.goto(-55, -95)
  ttl.goto(-45, -105)
  ttl.goto(-72, -122)
  ttl.penup()

  ttl.goto(-85, -139)
  ttl.pendown()
  ttl.goto(-100, -158)
  ttl.goto(-108, -153)
  ttl.goto(-88, -133)
  ttl.penup()

  ttl.goto(-102, -93)
  ttl.pendown()
  ttl.goto(-86, -122)
  ttl.goto(-90, -123)
  ttl.goto(-111, -99)
  ttl.penup()

  ttl.goto(-75, -139)
  ttl.pendown()
  ttl.goto(-60, -160)
  ttl.goto(-50, -153)
  ttl.goto(-73, -135)
  ttl.penup()

  #spokes wheel 1
  ttl.goto(-297, -110)
  ttl.pendown()
  ttl.goto(-300, -75)
  ttl.goto(-290, -75)
  ttl.goto(-293, -110)
  ttl.penup()

  ttl.goto(-297, -130)
  ttl.pendown()
  ttl.goto(-300, -165)
  ttl.goto(-290, -165)
  ttl.goto(-293, -130)
  ttl.penup()

  ttl.goto(-305, -125)
  ttl.pendown()
  ttl.goto(-340, -128)
  ttl.goto(-340, -118)
  ttl.goto(-305, -121)
  ttl.penup()

  ttl.goto(-285, -125)
  ttl.pendown()
  ttl.goto(-250, -128)
  ttl.goto(-250, -118)
  ttl.goto(-285, -121)
  ttl.penup()

  ttl.goto(-290, -111)
  ttl.pendown()
  ttl.goto(-270, -85)
  ttl.goto(-260, -95)
  ttl.goto(-287, -115)
  ttl.penup()

  ttl.goto(-290, -133)
  ttl.pendown()
  ttl.goto(-267, -154)
  ttl.goto(-258, -146)
  ttl.goto(-287, -128)
  ttl.penup()

  ttl.goto(-334, -102)
  ttl.pendown()
  ttl.goto(-303, -117)
  ttl.goto(-298, -112)
  ttl.goto(-327, -88)
  ttl.penup()

  ttl.goto(-298, -128)
  ttl.pendown()
  ttl.goto(-315, -160)
  ttl.goto(-325, -155)
  ttl.goto(-303, -128)
  ttl.penup()
  
  #arches
  ttl.setheading(90)
  ttl.goto(-240, -90)
  ttl.pencolor('blue')
  ttl.pendown()
  ttl.circle(55, 180)
  ttl.penup()

  ttl.setheading(90)
  ttl.goto(-15, -90)
  ttl.pendown()
  ttl.circle(67, 180)
  ttl.penup()

  ttl.setheading(90)
  ttl.goto(240, -90)
  ttl.pendown()
  ttl.circle(60, 180)
  ttl.penup()

  #persist drawing
  turtle.done()

main ()