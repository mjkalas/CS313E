#  File: ExpressionTree.py
#  Description: This program creates a tree from inputted equations.
#  Student's Name: Minal Kalas
#  Student's UT EID: mjk863
#  Course Name: CS 313E 
#  Unique Number: 50965
#  Date Created: 04/21/16
#  Date Last Modified: 04/23/16

class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.append ( item )

  def pop (self):
    return self.stack.pop()

  def peek (self):
    return self.stack[len(self.stack) - 1]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = Node(None)

  def createTree (self, expr):
    equation = expr.split()
    pare = Stack()
    curr = self.root

    for token in equation:
      if token == '(':
        pare.push(curr)
        curr.lChild = Node(None)
        curr = curr.lChild
      elif token in ['+', '-', '*', '/']:
        curr.data = token
        pare.push(curr)
        curr.rChild = Node(None)
        curr = curr.rChild
      elif token.isdigit() or '.' in token:
        curr.data = token
        curr = pare.pop()
      elif token == ')':
        if not pare.isEmpty():
          curr = pare.pop()
        else:
          break

  def evaluate (self, aNode):
    if aNode.data == '+':
      return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
    elif aNode.data == '-':
      return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild) 
    elif aNode.data == '*':
      return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
    elif aNode.data == '/':
      return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
      
    elif aNode.data.isdigit() or '.' in aNode.data:
      return eval(aNode.data)

  def preOrder (self, aNode):
    if (aNode != None):
      print(aNode.data, end = ' ')
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)

  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      print(aNode.data, end = ' ')

def main():
  in_file = open("expression.txt", "r")
  data = in_file.readline()
  tree = Tree()
  tree.createTree(data)
  print(data, '=', tree.evaluate(tree.root), "\n")
  
  # Print prefix and postfix versions of the expression
  print("Prefix Expression:", end = ' ') 
  tree.preOrder(tree.root)
  print("\n")
  print("Postfix Expression:", end = ' ')
  tree.postOrder(tree.root)
main()