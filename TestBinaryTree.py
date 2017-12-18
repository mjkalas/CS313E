import random

def main():
  
  #treeA = treeB & tree 3 is different.
  treeA = Tree()
  treeA.insert(50)
  treeA.insert(30)
  treeA.insert(70)
  treeA.insert(10)
  treeA.insert(40)
  treeA.insert(60)
  treeA.insert(80)
  treeA.insert(7)
  treeA.insert(25)
  treeA.insert(38)
  treeA.insert(47)
  treeA.insert(58)
  treeA.insert(65)
  treeA.insert(77)
  treeA.insert(96)
  
  treeB = Tree()
  treeB.insert(50)
  treeB.insert(30)
  treeB.insert(70)
  treeB.insert(10)
  treeB.insert(40)
  treeB.insert(60)
  treeB.insert(80)
  treeB.insert(7)
  treeB.insert(25)
  treeB.insert(38)
  treeB.insert(47)
  treeB.insert(58)
  treeB.insert(65)
  treeB.insert(77)
  treeB.insert(96)
  
  #treeC is random
  treeC = Tree()
  nums = random.randint(0, 20)
  for i in range(nums):
    treeC.insert(random.randint(1, 50))
    
  # Test isSimilar()
  print("\nTree A and Tree B are similar: ", treeA.isSimilar(treeB))
  print("Tree B and Tree C are similar: ", treeB.isSimilar(treeC))
  
  # Test printLevel()
  print("\nThe levels of Tree A are:")
  for i in range(1, 5):
    treeA.printLevel(i)
    
  print("\nThe levels of Tree C are:")
  for j in range(1, 16):
    treeC.printLevel(j)
  
  # Test getHeight()
  print("\nThe height of Tree A is: ", treeA.getHeight())
  print("The height of Tree C is: ", treeC.getHeight())

  # Test numNodes()
  print("The number of nodes in Tree B is: ", treeB.numNodes())
  print("The number of nodes in Tree C is: ", treeC.numNodes())
  print()

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Check 2 binary trees
  def isSimilar(self, other):
    anode = self.root
    bnode = other.root
    return self.compareNodes(anode, bnode)
    
  def compareNodes(self, anode, bnode):
    if anode == None and bnode == None:
      return True
      
    if anode == None and bnode != None:
      return False
    elif anode != None and bnode == None:
      return False
    elif anode.data != bnode.data:
      return False
    else:
      return self.compareNodes(anode.lChild, bnode.lChild) and \
      self.compareNodes(anode.rChild, bnode.rChild)
    
  # Prints nodes at a given level
  def printLevel(self, level):
    nodes = []
    self.findLevel(level, 1, nodes, self.root)
    if len(nodes) == 0:
      return 
    else:
      print(nodes)
    
  # Helper for printLevel
  def findLevel(self, level, currlvl, lst, aNode):
    if currlvl > level:
      return
    
    if aNode == None:
      return
    else:
      if currlvl == level:
        lst.append(aNode.data)
      else:
        self.findLevel(level, currlvl + 1, lst, aNode.lChild)
        self.findLevel(level, currlvl + 1, lst, aNode.rChild)
    
  # Return the height of the tree
  def getHeight(self):
    aHeights = [0]
    self.height_count(self.root, 0, aHeights)
    aHeights.sort()
    return aHeights[-1]   
    
  # Helper for getHeight
  def height_count(self, aNode, pathLength, aHeights):
    if aNode == None:
      aHeights.append(pathLength)
    else:
      pathLength += 1
      self.height_count(aNode.lChild, pathLength, aHeights)
      self.height_count(aNode.rChild, pathLength, aHeights)
          
  # Return number of nodes in the left subtree and the nodes in the right subtree
  def numNodes(self):
    nodes = self.nodeCount(self.root)
    return nodes
    
  # Keeps count for numNodes()  
  def nodeCount(self, aNode):
    if aNode == None:
      return 0
    else:
      return 1 + self.nodeCount(aNode.lChild) + self.nodeCount(aNode.rChild) 
  
  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current


  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode


  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lChild)
      print (aNode.data)
      self.inOrder (aNode.rChild)


  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)


  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      print (aNode.data)


  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent


  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent


  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True
    
main()
