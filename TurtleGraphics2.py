import turtle

def drawSquares(ttl, x, y, side):
	ttl.penup ()
	ttl.goto (x, y)
	ttl.setheading(0)
	ttl.pendown()
	for inter in range (4):
		ttl.forwad(side)
		ttl.riht(90)
	ttl.penup()

def main():
	#put label on top of page
	turtle.title ("Squares")

	#set up screen size
	turtle.setup(800, 800, 0. 0)

	#create a turtle object
	ttl = turtle.Turtle()

	#decide on the shape
	ttl.shape ("turtle")

	ttl.

def drawLine(ttl, x1, y1, x2, y2):
	ttl.penup()
	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

def drawPolygon