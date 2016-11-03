#  File: Josephus.py
#  Description:Uses a circular linked list to determine where Josephus would need to be to live.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 313E
#  Unique Number: 40965
#  Date Created: 04/10/16
#  Date Last Modified: 04/10/16

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ): 
    self.first = None

  # Insert an element in the list
  def insert ( self, item ):
    newLink = Link(item)
    if self.first == None:
      self.first = newLink
      self.first.next = self.first
      return
    else:
      curr = self.first
      while(curr.next != self.first):
        curr = curr.next
      curr.next = newLink
      curr = curr.next
      curr.next = self.first
      return

  # Find the link with the given key
  def find ( self, key ):
    curr = self.first
    if curr == None:
      return None
    else:
      if curr.next == self.first and curr.data == key:
        return curr
    while (curr.next != self.first):
      if curr.data == key:
        return curr
      else:
        curr = curr.next
    if curr.data == key:
      return curr
    else:
      return None


  # Delete a link with a given key
  def delete ( self, key ):
    curr = self.first
    prev = self.first
    while prev.next != self.first:
      prev = prev.next
    if curr == None:
      return None
    else:
      if curr.next == self.first and curr.data == key:
        return curr
    while (curr.data != key):
      if curr.next == self.first:
        return None
      else:
        prev = curr
        curr = curr.next
    if curr == self.first:
      self.first = self.first.next
    prev.next = curr.next
    return curr


  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):
    start_pos = self.first
    deadguys = ""
    while start != 1:
      start_pos = start.pos.next
      start -= 1

    while start_pos.next != start_pos:
      for i in range(n - 1):
        start_pos = start_pos.next
      value = start_pos.data
      deadguy = self.delete(value)
      deadguys += str(deadguy.data) + " "
      start_pos = start_pos.next
    print (deadguys)
    print(start_pos.data)

  # Return a string representation of a Circular List
  def __str__ ( self ):
    curr = self.first
    if curr == None:
      return "The List is Empty."
    temp = str(curr.data)
    temp += " "
    while curr.next != self.first:
      temp += str(curr.next.data)
      curr = curr.next
      temp += " "
    result = temp[0:-1]
    return result

def main():
  in_file = open("josephus.txt", "r")
  soldiers = int(in_file.readline())
  start = int(in_file.readline())
  increment = int(in_file.readline())
  CircList = CircularList()
  for i in range (1, soldiers + 1):
    CircList.insert(i)
  if CircList.first != None:
    CircList.deleteAfter(start, increment)
  else:
    print(CircList)

main()