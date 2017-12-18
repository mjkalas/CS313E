class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def getNumLinks (self):
    cnt = 0
    curr = self.first
    while curr != None:
      cnt += 1
      curr = curr.next
    return cnt

  def addFirst (self, data): 
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def addLast (self, data):
    newLink = Link (data)
    curr = self.first
    if (curr == None):
      self.first = newLink
      return
    while (curr.next != None):
      curr = curr.next
    curr.next = newLink

  def addInOrder (self, data):
    if self.first == None:
        self.addFirst(data)
        return
    if data < self.first.data:
        self.addFirst(data)
        return
    else:
        newLink = Link(data)
        curr = self.first
        prev = self.first
        while (data > curr.data):
            if curr.next == None:
                self.addLast(data)
                return
            else:
                prev = curr
                curr = curr.next
        prev.next = newLink
        newLink.next = curr

  def findUnordered (self, data):
    curr = self.first
    if curr == None:
        return None
    else:
        while (curr.data != data):
            if curr.next == None:
                return None
            else:
                curr = curr.next
        return curr

  def findOrdered (self, data):
    curr = self.first
    if curr == None:
        return None
    else:
        while (curr.data != data):
            if curr.next == None:
                return None
            else:
                if curr.next.data > data:
                    return None 
                else:
                    curr = curr.next
        return curr

  def delete (self, data):
    curr = self.first
    prev = self.first

    if (curr == None):
      return None

    while (curr.data != data):
      if (curr.next == None):
        return None
      else:
        prev = curr
        curr = curr.next

    if (curr == self.first):
      self.first = self.first.next
    else:
      prev.next = curr.next

    return curr

  def __str__ (self):
    curr = self.first
    cnt = 0
    strng = ''    
    if self.isEmpty():
      return 'LinkedList is Empty'
    
    for i in range(self.getNumLinks() - 1):
      strng += str(curr.data) + '  '
      curr = curr.next
      cnt += 1
      if (cnt - 1) % 10 == 0:
        strng += '\n '
    
    strng += str(curr.data)
    return strng

  def copyList (self):
    copy_LinkedList = LinkedList()
    curr = self.first
    while (curr != None):
        copy_LinkedList.addLast(curr.data)
        curr = curr.next
    return copy_LinkedList

  def reverseList (self):
    reverse_LinkedList = LinkedList()
    curr = self.first
    while (curr != None):       
        reverse_LinkedList.addFirst(curr.data)
        curr = curr.next
    return reverse_LinkedList

  def sortList (self): 
    sortedLinked = LinkedList()
    if self.isEmpty():
      return sortedLinked

    curr = self.first
    for i in range(self.getNumLinks()):
      sortedLinked.addInOrder(curr.data)
      curr = curr.next  
      
    return sortedLinked

  def isSorted (self):
    curr = self.first
    if self.isEmpty() or self.getNumLinks() == 1:
      return True
      
    for i in range(self.getNumLinks() - 1):
      if curr.data > curr.next.data:
        return False
      curr = curr.next
      
    return True 

  def isEmpty (self): 
    return (self.first == None)

  def mergeList (self, b): 
    curr = b.first
    merged = self.copyList().sortList()

    if self.isEmpty():
      if b.isEmpty():
        return merged
      else:
        merged = b.copyList()
        return merged
    elif b.isEmpty():
      return merged

    for i in range(b.getNumLinks()):
      merged.addInOrder(curr.data)
      curr = curr.next
      
    return merged

  def isEqual (self, b):
    if self.getNumLinks() != b.getNumLinks():
      return False
      
    if self.isEmpty() and b.isEmpty():
      return True
      
    curr1 = self.first
    curr2 = b.first
    
    for i in range(self.getNumLinks()):
      if curr1.data != curr2.data:
        return False
      curr1 = curr1.next
      curr2 = curr2.next
      
    return True

  def removeDuplicates (self):
    rem = self.copyList()
    prev = rem.first
    curr = rem.first
    elmnts = []

    for i in range(rem.getNumLinks()):
      if curr.data in elmnts:
        curr = curr.next
        prev.next = curr
      else:
        elmnts.append(curr.data)
        prev = curr
        curr = curr.next
        
    return rem

def main():
  # Test methods addFirst() and __str__() by adding more than 10 items to a list and printing it.
  print("Testing addFirst() & __str__().")
  test = LinkedList()
  for i in range (0, 10):
    test.addFirst(i)
  print(test)
  print("\n")

  # Test method addLast()
  print("Testing addLast().")
  for i in range (10, 20):
    test.addLast(i)
  print(test)
  print("\n")

  # Test method addInOrder()
  print("Testing addInOrder().")
  for i in range (30, 20, -1):
    test.addInOrder(i)
  print(test)
  print("\n")

  # Test method getNumLinks()
  print("Testing getNumLinks().")
  print(test.getNumLinks())
  print("\n")

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there 
  print("Testing findUnordered().")
  print(test.findUnordered(29))
  print (test.findUnordered(35))
  print("\n")

  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there
  print("Testing findOrdered().")
  print(test.findOrdered(15))
  print(test.findOrdered(36))  
  print("\n")

  # Test method delete()
  # Consider two cases - item is there, item is not there 
  print("Testing delete().")
  print(test.delete(1))
  print(test.delete(100))
  print("\n")

  # Test method copyList()
  print("Testing copyList().")
  print(test.copyList())
  print("\n")

  # Test method reverseList()
  print("Testing reverseList().")
  print(test.reverseList())
  print("\n")

  # Test method sortList()
  print("Testing sortList().")
  print(test.sortList())
  print("\n")

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print("Testing isSorted().")
  print(test.isSorted())
  test2 = LinkedList()
  test2.addFirst(50)
  test2.addFirst(45)
  print(test2)
  print("\n")

  # Test method isEmpty()
  print("Testing isEmpty().")
  test3 = LinkedList()
  print(test.isEmpty())
  print("test3: " + str(test3.isEmpty()))
  print("\n")

  # Test method mergeList()
  print("Testing method mergeList().")
  test4 = LinkedList()
  for i in range (35, 45, 2):
    test4.addLast(i)
  test5 = LinkedList()
  for i in range (40, 50, 2):
    test5.addLast(i)

  merged = test4.mergeList(test5)
  print(merged)
  print("\n")

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print("Testing isEqual().")
  print(test4.isEqual(test4))
  print(test4.isEqual(test5))
  print("\n")

  # Test removeDuplicates()
  print("Testing removeDuplicates().")
  test6 = LinkedList()
  for i in range (1, 10):
    test6.addLast(1)
    test6.addLast(2)
  removed = test6.removeDuplicates()
  print(removed)
  print("\n")

main()
