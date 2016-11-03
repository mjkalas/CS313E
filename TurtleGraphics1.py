import turtle

def main():
  #put label on top of page
  turtle.title('Hello World')

  #setup screem size
  turtle.setup (1000, 1000, 0, 0)

  #move turtle to origin
  turtle.penup()
  turtle.goto (0, 0)

  #set the colour to navy
  turtle.color ('navy')

  #write the message
  turtle.write ('Hello World!', font = ('Helvetica', 36, 'bold'))

  #finish the drawing
  turtle.done()
main()