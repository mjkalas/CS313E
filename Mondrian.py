import turtle
import random

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# draw a square of a given side 
# starting at uuper left corner (x, y)
def drawSquare (ttl, colour, xneg, yneg, xpos, ypos):
  ttl.color('black', colour)
  ttl.penup()
  ttl.goto(xneg, yneg)
  ttl.begin_fill()
  ttl.pendown()
  ttl.goto(xpos, yneg)
  ttl.goto(xpos, ypos)
  ttl.goto(xneg, ypos)
  ttl.goto(xneg, yneg)
  ttl.end_fill()
  ttl.color('black')

def colour (ttl, level, xneg, yneg, xpos, ypos):
  colour = random.randint(1, 5)
  if colour == 1: 
    colour = 'red'
  elif colour == 2:
    colour = 'white'
  elif colour == 3:
    colour = 'black'
  elif colour == 4:
    colour = 'yellow' 
  elif colour == 5:
    colour = 'blue'

  drawSquare(ttl, colour, xneg, yneg, xpos, ypos)

def direction(ttl, level):
  if level == 1:
    choice = random.randint(1, 2)
    return choice
  else:
    rand_num = random.randint(1, 5)
    if level == 2 and rand_num == 1:
        choice = 3
    elif level == 3 and rand_num == 2:
        choice = 3
    elif level == 4 and rand_num == 3:
        choice = 3
    elif level == 5 and rand_num == 4:
        choice = 3
    elif level == 6 and rand_num == 5:
        choice = 3
    else:
      choice = random.randint(1, 2)
  return choice


def recursive_mondrian(ttl, level, xneg, xpos, yneg, ypos):
  if level == 0:
    return
  else:
    choice = direction(ttl, level)
    if choice == 1:
      if (xpos - (25 // level)) - (xneg + (25 // level)) > 0:
        x = random.randint((xneg + (25 // level)), (xpos - (25 // level)))
      else:
        x = (xneg + xpos) // 2
      drawLine(ttl, x, yneg, x, ypos)

      if level == 1:
        colour(ttl, level, x, yneg, xpos, ypos)
      recursive_mondrian(ttl, level - 1, x, xpos, yneg, ypos)
      recursive_mondrian(ttl, level - 1, xneg, x, yneg, ypos)

    elif choice == 2:
      if (ypos - (25 // level)) - (yneg + (25 // level)) > 0:
        y = random.randint((yneg + (25 // level)), (ypos - (25 // level)))
      else:
        y = (yneg + ypos) // 2
      drawLine(ttl, xneg, y, xpos, y)

      if level == 1:
        colour(ttl, level, xneg, y, xpos, ypos)
      recursive_mondrian(ttl, level - 1, xneg, xpos, y, ypos)
      recursive_mondrian(ttl, level -1, xneg, xpos, yneg, y)

    else:
      recursive_mondrian(ttl, level - 1, xneg, xpos, yneg, ypos)


def main():
  # put label on top of page
  turtle.title ('Mondrian')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  print("Mondrian Composition")
  level = int(input("Enter a level of recurstion between 1 and 6: "))

  ttl.pensize (6)
  ttl.color('black')

  recursive_mondrian(ttl, level, -350, 350, -350, 350)

  ttl.penup()
  ttl.goto(-350, -350)
  ttl.pendown()
  ttl.goto(-350, 350)
  ttl.goto(350, 350)
  ttl.goto(350, -350)
  ttl.goto(-350, -350)
  ttl.penup()
  canvas = turtle.getscreen().getcanvas()
  canvas.postscript(file = './Mondrian.eps')

  # persist drawing

  turtle.done()

main()

