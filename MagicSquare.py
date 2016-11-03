'''
File: MagicSquare.py
Description: This program makes a magic square from a given odd number.
Student's Name: Minal Kalas
Student's UT EID: mjk863
Course Name: CS 313E 
Unique Number: 50945
Date Created:02/04/16
Date Last Modified: 02/06/16
'''

def incrementIndex (index, n):
  index = index+1
  if index > n-1:
    index = 0
  return index

def makeSquare(n):
  square = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(0)
    square.append(row)
  
  indexr = 0
  indexc = 0

  for i in range (1, n*n+1):
    if i == 1:
      square[n-1][int((n-1)/2)] = 1
      indexr = n-1
      indexc = int((n-1)/2)
    else:
      square[indexr][indexc] = i
    indexr2 = incrementIndex(indexr, n)
    indexc2 = incrementIndex(indexc, n)
    if square[indexr2][indexc2] > 0:
      indexr = indexr-1
      indexc = indexc
    elif (indexr == n-1) and (indexc == n-1):
      indexr = indexr-1
      indexc = indexc-1
    else:
      indexr = indexr2
      indexc = indexc2

  return square

def printSquare(square):           
  for i in square:
    for j in i:
      print(format(j, '2d'), end = " ")
    print()

def checkSquare (magicSquare, n):
  magic_square = True    
  for column in range(n):
    total = 0
    for i in range(n):
      total += magicSquare[i][column]
    if total != (n*((n**2)+1)/2):
      magic_square = False
  for i in range(n):
    for j in range (i):
      if sum(square[i])!= (n*((n**2)+1)/2):
        magic_square = False
      if sum(square[i][j]) != (n*((n**2)+1)/2):
        magic_square = False
      if square[j][i] != (n*((n**2)+1)/2):
          magic_square = False

    return magic_square            
        
def main():
  n = int(input("Please enter an odd number:"))
  while (n % 2 != 1) or (n < 3):
    n = int(input("Please enter an odd number:"))

  square = makeSquare(n)
  magic_square = checkSquare(square, n)

  if magic_square == True:
    print("Here is a", n, "x", n, "magic square:")
    print()
    printSquare(square)
    print()
    print("Sum of row = ", int(n*((n**2)+1)/2))
    print("Sum of column = ", int(n*((n**2)+1)/2))
    print("Sum diagonal (UL to LR) = ", int(n*((n**2)+1)/2))
    print("Sum diagonal (UR to LL) = ", int(n*((n**2)+1)/2))
    
main()