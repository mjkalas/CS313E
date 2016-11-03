#  File: Triangle.py
#  Description:  This program calculates the greatest path sum through various algorithms.
#  Student's Name: Minal Kalas
#  Student's UT EID: mjk863
#  Course Name: CS 313E 
#  Unique Number: 50945
#  Date Created: 04/18/16
#  Date Last Modified: 04/18/16

# returns the greatest path sum using exhaustive search
def exhaustive_search (triangle, index, i, b, c):
  if i == (len(triangle)):
    b.append(c)
  else: 
    c += triangle[i][index]
    return exhaustive_search(triangle, index, i + 1, b, c) or exhaustive_search(triangle, index + 1, i + 1, b, c)

# returns the greatest path sum using greedy approach
def greedy (triangle):
  index = 0
  c = 0
  for i in range(len(triangle) - 1):
    c += triangle[i][index]
    if (triangle[i + 1][index] > triangle[i + 1][index + 1]):
      index = index
    else:
      index = index + 1
  c += triangle[i + 1][index]
  return c

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (triangle, c, b):
  if len(triangle) == 1:
    b.append(c + triangle[0][0])
  else:
    triangle1 = []
    triangle2 = []
    for line in triangle[1:]:
      triangle1.append(line[1:])
      triangle2.append(line[:-1])
    c = c + triangle[0][0]
    return (rec_search(triangle1, c, b)) or (rec_search(triangle2, c, b))

# returns the greatest path sum using dynamic programming
def dynamic_prog (triangle):
  total = triangle[-1]
  for i in range(len(triangle) - 1, 0, -1):
    line1 = triangle[i - 1]
    line2 = total
    total = []
    for j in range(len(line1)):
      total.append(max((line1[j] + line2[j]), (line1[j] + line2[j + 1]))) 
  return total[0]

# reads the file and returns a 2-D list that represents the triangle
def readFile (file):
  triangle=[]
  file.readline()
  for line in file:
    line = line.split()
    line = [int(i) for i in line]
    triangle.append(line)
  return triangle

def main ():
  
  # read triangular triangle from file
  triangle = []
  in_file = open("triangle.txt","r")
  triangle = readFile(in_file)
  
  # output greates path from exhaustive search
  b = []
  exhaustive_search (triangle, 0, 0, b, 0)
  print("The greatest path sum through exhaustive search is " + str(max(b)) + ".")
  
  # output greates path from greedy approach
  print("The greatest path sum through greedy search is " + str(greedy(triangle)) + ".")
  
  # output greates path from divide-and-conquer approach
  a = []
  rec_search(triangle, 0, a)
  print("The greatest path sum through recursive search is " + str(max(a)) + ".")
  
  # output greates path from dynamic programming 
  print("The greatest path sum through exhaustive search is " + str(dynamic_prog(triangle)) + ".")
main()