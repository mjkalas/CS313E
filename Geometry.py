#  File: Geometry.py
#  Description: This program takes in a file with coordinates and gives output of general location in 3D space.
#  Student Name: Minal Kalas
#  Student UT EID: mjk863
#  Course Name: CS 313E
#  Unique Number: 50945
#  Date Created: 02/19/16
#  Date Last Modified: 02/21/16

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point (x, y, z)
  def __str__ (self):
    s = '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    return s

  # get distance to another Point object
  def distance (self, other):
    x2 = (self.x - other.x) * (self.x - other.x)
    y2 = (self.y - other.y) * (self.y - other.y)
    z2 = (self.z - other.z) * (self.z - other.z)
    return ((x2 + y2 + z2) ** 0.5)

  # test for equality between two points
  def is_equal (a, b):
    tol = 1.0e-16
    return (abs (x - y) < tol)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point (x, y, z)
    self.radius = radius

  # string representation of a Sphere: Center: (x, y, z), Radius: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Radius: " + str(self.radius)
    return s

  # compute surface area of Sphere
  def area (self):
    return 4 * math.pi * self.radius * self.radius

  # compute volume of a Sphere
  def volume (self):
    return (4 / 3) * math.pi * ((self.radius) ** 3)

  # determines if a Point is strictly inside the Sphere
  def is_inside_point (self, p):
    dist = p.distance (self.center)
    return (dist < self.radius)

  # determine if another Sphere is strictly inside this Sphere
  def is_inside_sphere (self, other):
    dist = self.center.distance (other.center)
    return (self.radius > (dist + other.radius))

  # determine if a Cube is strictly inside this Sphere
  def is_inside_cube (self, a_cube):
    x_positive = (a_cube.center.x + a_cube.side/2)
    x_negative = (a_cube.center.x - a_cube.side/2)
    y_positive = (a_cube.center.y + a_cube.side/2)
    y_negative = (a_cube.center.y - a_cube.side/2)
    z_positive = (a_cube.center.z + a_cube.side/2)
    z_negative = (a_cube.center.z - a_cube.side/2)
   
    point_1 = Point(x_negative, y_negative, z_negative)
    point_2 = Point(x_negative, y_negative, z_positive)
    point_3 = Point(x_negative, y_positive, z_negative)
    point_4 = Point(x_negative, y_positive, z_positive)
    point_5 = Point(x_positive, y_negative, z_negative)
    point_6 = Point(x_positive, y_negative, z_positive)
    point_7 = Point(x_positive, y_positive, z_negative)
    point_8 = Point(x_positive, y_positive, z_positive)

    return (self.is_inside_point(point_1) and self.is_inside_point(point_2) and self.is_inside_point(point_3) and self.is_inside_point(point_4) and self.is_inside_point(point_5) and self.is_inside_point(point_6) and self.is_inside_point(point_7) and self.is_inside_point(point_8))

  # (optional) determine if a Cylinder is strictly inside this Sphere
  # def is_inside_cylinder (self, a_cyl):

  # determine if another Sphere intersects this Sphere
  # there is a non-zero volume of intersection

  def does_intersect_sphere (self, other):
    dist = self.center.distance (other.center)
    return (dist < (self.radius + other.radius))

  # determine if a Cube intersects this Sphere
  # there is a non-zero volume of intersection
  def does_intersect_cube (self, a_cube):
    x_positive = (a_cube.center.x + a_cube.side/2)
    x_negative = (a_cube.center.x - a_cube.side/2)
    y_positive = (a_cube.center.y + a_cube.side/2)
    y_negative = (a_cube.center.y - a_cube.side/2)
    z_positive = (a_cube.center.z + a_cube.side/2)
    z_negative = (a_cube.center.z - a_cube.side/2)

    if (self.center.x >= x_negative and self.center.x <= x_positive):
      centerx = self.center.x
    elif (self.center.x < x_negative):
      centerx = x_negative
    else:
      centerx = x_positive

    if (self.center.y >= y_negative and self.center.y <= y_positive):
      centery = self.center.y
    elif (self.center.y < y_negative):
      centery = y_negative
    else:
      centery = y_positive

    if (self.center.z >= z_negative and self.center.z <= z_positive):
      centerz = self.center.z
    elif (self.center.z < z.negative):
      centerz = z_negative
    else:
      centerz = z_positive

    return (self.radius > self.center.distance(Point(centerx, centery, centerz)))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  def circumscribe_cube (self):
    return (Cube(self.center.x, self.center.y, self.center.z, round(self.radius*2/(3**.5), 3)))

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = side

  # string representation of a Cube: Center: (x, y, z), Side: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Side: " + str(self.side)
    return s

  # compute surface area of Cube
  def area (self):
    return (6 * (self.side ** 2))

  # compute volume of a Cube
  def volume (self):
    return (self.side ** 3)

  # determines if a Point is strictly inside this Cube
  def is_inside_point (self, p):
    distx = math.fabs(self.center.x - p.x)
    disty = math.fabs(self.center.y - p.y)
    distz = math.fabs(self.center.z - p.z)
    half = self.side/2

    return ((distx < half) and (disty < half) and (distz < half))

  # determine if a Sphere is strictly inside this Cube
  def is_inside_sphere (self, a_sphere):
    is_inside = self.is_inside_cube(Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z))
    return (is_inside)

  # determine if another Cube is strictly inside this Cube
  def is_inside_cube (self, other):
    x_positive = (other.center.x + other.side/2)
    x_negative = (other.center.x - other.side/2)
    y_positive = (other.center.y + other.side/2)
    y_negative = (other.center.y - other.side/2)
    z_positive = (other.center.z + other.side/2)
    z_negative = (other.center.z - other.side/2)

    point_1 = Point(x_negative, y_negative, z_negative)
    point_2 = Point(x_negative, y_negative, z_positive)
    point_3 = Point(x_negative, y_positive, z_negative)
    point_4 = Point(x_negative, y_positive, z_positive)
    point_5 = Point(x_positive, y_negative, z_negative)
    point_6 = Point(x_positive, y_negative, z_positive)
    point_7 = Point(x_positive, y_positive, z_negative)
    point_8 = Point(x_positive, y_positive, z_positive)

    return (self.is_inside_point(point_1) and self.is_inside_point(point_2) and self.is_inside_point(point_3) and self.is_inside_point(point_4) and self.is_inside_point(point_5) and self.is_inside_point(point_6) and self.is_inside_point(point_7) and self.is_inside_point(point_8))

  # determine if a Cylinder is strictly inside this Cube
  def is_inside_cylinder (self, a_cyl):
    height = a_cyl.height
    half = self.side/2
    horiz_x = (self.center.x + half > a_cyl.center.x + a_cyl.center.x) and (self.center.x - half < a_cyl.center.x - height)
    horiz_y = (self.center.y + half > a_cyl.center.y + a_cyl.center.y) and (self.center.y - half < a_cyl.center.y - height)
    vert = (self.center.z + half > a_cyl.center.z + a_cyl.center.z) and (self.center.z - half < a_cyl.center.z - height)

    return (vert and horiz_x and horiz_x)

  # determine if another Cube intersects this Cube
  # there is a non-zero volume of intersection
  def does_intersect_cube (self, other):
    x_positive = (other.center.x + other.side/2)
    x_negative = (other.center.x - other.side/2)
    y_positive = (other.center.y + other.side/2)
    y_negative = (other.center.y - other.side/2)
    z_positive = (other.center.z + other.side/2)
    z_negative = (other.center.z - other.side/2)

    point_1 = Point(x_negative, y_negative, z_negative)
    point_2 = Point(x_negative, y_negative, z_positive)
    point_3 = Point(x_negative, y_positive, z_negative)
    point_4 = Point(x_negative, y_positive, z_positive)
    point_5 = Point(x_positive, y_negative, z_negative)
    point_6 = Point(x_positive, y_negative, z_positive)
    point_7 = Point(x_positive, y_positive, z_negative)
    point_8 = Point(x_positive, y_positive, z_positive)

    return (self.is_inside_point(point_1) or self.is_inside_point(point_2) or self.is_inside_point(point_3) or self.is_inside_point(point_4) or self.is_inside_point(point_5) or self.is_inside_point(point_6) or self.is_inside_point(point_7) or self.is_inside_point(point_8))

  # determine the volume of intersection if this Cube intersects with another Cube
  def intersection_volume (self, other):
    if (self.side > other.side):
      cube_greater = self
      cube_lesser = other
    else:
      cube_greater = other
      cube_lesser = self

    lside_half = cube_lesser.side/2
    gside_half = cube_greater.side/2

    if (self.does_intersect_cube(other)):
      distx = min(cube_lesser.center.x + lside_half, cube_greater.center.x + gside_half) - max(cube_lesser.center.x - lside_half, cube_greater.center.x-gside_half)
      disty = min(cube_lesser.center.y + lside_half, cube_greater.center.y + gside_half) - max(cube_lesser.center.y - lside_half, cube_greater.center.y-gside_half)
      distz = min(cube_lesser.center.z + lside_half, cube_greater.center.z + gside_half) - max(cube_lesser.center.z - lside_half, cube_greater.center.z-gside_half)
      return (distx*disty*distz)
    else:
      return 0

  # return the largest Sphere object that is inscribed
  # by this Cube
  def inscribe_sphere (self):
    return (Sphere(self.center.x, self.center.y, self.center.z, self.side/2))

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point(x, y, z)
    self.radius = radius
    self.height = height

  # string representation of a Cylinder: Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Radius: " + str(self.radius) + ", Height: " + str(self.height)
    return s

  # compute surface area of Cylinder
  def area (self):
    return ((2 * math.pi * (self.radius ** 2)) + (self.height * 2 * math.pi * self.radius))

  # compute volume of a Cylinder
  def volume (self):
    return (math.pi * (self.radius ** 2) * self.height)

  # determine if a Point is strictly inside this Cylinder
  def is_inside_point (self, p):
    math.fabs(self.center.z-p.z)<self.height/2
    math.hypot((self.center.x-p.x),(self.center.y-p.y))<self.radius
    return ()

  # determine if a Sphere is strictly inside this Cylinder
  def is_inside_sphere (self, a_sphere):
    disthypot = (math.hypot((self.center.x-a_sphere.center.x),(self.center.y-a_sphere.center.y))+a_sphere.radius < self.radius)
    distz_inside = (a_sphere.center.z<self.center.z+self.height-a_sphere.radius)
    distz_outside = (a_sphere.center.z>self.center.z-self.height+a_sphere.radius)

    return (disthypot and distz_inside and distz_outside)

  # determine if a Cube is strictly inside this Cylinder
  def is_inside_cube (self, a_cube):
    x_positive = (a_cube.center.x + a_cube.side/2)
    x_negative = (a_cube.center.x - a_cube.side/2)
    y_positive = (a_cube.center.y + a_cube.side/2)
    y_negative = (a_cube.center.y - a_cube.side/2)
    z_positive = (a_cube.center.z + a_cube.side/2)
    z_negative = (a_cube.center.z - a_cube.side/2)

    point_1 = Point(x_negative, y_negative, z_negative)
    point_2 = Point(x_negative, y_negative, z_positive)
    point_3 = Point(x_negative, y_positive, z_negative)
    point_4 = Point(x_negative, y_positive, z_positive)
    point_5 = Point(x_positive, y_negative, z_negative)
    point_6 = Point(x_positive, y_negative, z_positive)
    point_7 = Point(x_positive, y_positive, z_negative)
    point_8 = Point(x_positive, y_positive, z_positive)

    return (self.is_inside_point(point_1) and self.is_inside_point(point_2) and self.is_inside_point(point_3) and self.is_inside_point(point_4) and self.is_inside_point(point_5) and self.is_inside_point(point_6) and self.is_inside_point(point_7) and self.is_inside_point(point_8))


  # determine if another Cylinder is strictly inside this Cylinder
  def is_inside_cylinder (self, other):
    half_heighto = other.height/2
    height = self.height
    center_self = Point(self.center.x, self.center.y, 0)
    center_other = Point(other.center.x, other.center.y, 0)
    vert = (self.center.z > other.center.z + half_heighto) and (self.center.z - height < other.center.z - half_heighto)
    dist_centers = center_self.distance(center_other)

    return (self.radius > other.radius + dist_centers) and vert

  # (optional) determine if another Cylinder intersects this Cylinder
  # there is a non-zero volume of intersection
  # def does_intersect_cylinder (self, other):

def main():
  input_file = []
  # open file "geometry.txt" for reading\
  in_file = open("./geometry.txt", "r")
  for line in in_file:
    line = line.split (" ")
    input_file.append (line)

  # read the coordinates of the first Point p
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      Point_p = Point(float(input_file[0][0]), float(input_file [0][1]), float(input_file[0][2]))
  print ("Point p: " + str(Point_p))

  # read the coordinates of the second Point q
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      Point_q = Point(float(input_file[1][0]), float(input_file [1][1]), float(input_file[1][2]))
  print ("Point q: " + str(Point_q))

  # read the coordinates of the center and radius of sphereA
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      sphereA = Sphere (float(input_file[2][0]), float(input_file [2][1]), float(input_file[2][2]), float(input_file[2][3]))
  print ("sphereA: " + str(sphereA))

  # read the coordinates of the center and radius of sphereB
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      sphereB = Sphere (float(input_file[3][0]), float(input_file [3][1]), float(input_file[3][2]), float(input_file[3][3]))
  print ("sphereB: " + str(sphereB))

  # read the coordinates of the center and side of cubeA
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      cubeA = Cube (float(input_file[4][0]), float(input_file [4][1]), float(input_file[4][2]), float(input_file[4][3]))
  print ("cubeA: " + str(cubeA))

  # read the coordinates of the center and side of cubeB
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      cubeB = Cube (float(input_file[5][0]), float(input_file [5][1]), float(input_file[5][2]), float(input_file[5][3]))
  print ("cubeB: " + str(cubeB))

  # read the coordinates of the center, radius and height of cylA
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      cylA = Cylinder(float(input_file[6][0]), float(input_file [6][1]), float(input_file[6][2]), float(input_file[6][3]), float(input_file[6][4]))
  print ("cylA: " + str(cylA))

  # read the coordinates of the center, radius and height of cylB
  for i in range (len(input_file)):
    for j in range (len(input_file[i])):
      cylB = Cylinder(float(input_file[7][0]), float(input_file [7][1]), float(input_file[7][2]), float(input_file[7][3]), float(input_file[7][4]))
  print ("cylB: " + str(cylB))

  # close file geometry.txt
  in_file.close

  # print distance between p and q
  print()
  print("Distance between p and q: ",(Point_p.distance(Point_q)))
  print ()

  # print area of sphereA
  print ("Area of sphereA: " ,(sphereA.area()))

  # print volume of sphereA
  print ("Volume of sphereA: " ,(sphereA.volume()))

  # print if Point p is inside sphereA
  if (sphereA.is_inside_point(Point_p)):
    print ("Point p is inside sphereA")
  else:
    print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if (sphereA.is_inside_sphere(sphereB)):
    print ("sphereB is inside sphereA")
  else:
    print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if (sphereA.is_inside_cube(cubeA)):
    print ("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")

  # (optional) print if cylA is inside sphereA

  # print if sphereA intersects with sphereB
  if (sphereA.does_intersect_sphere(sphereB)):
    print ("sphereA does intersect sphereB")
  else:
    print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if (sphereB.does_intersect_cube(cubeB)):
    print ("sphereA does intersect sphereB")
  else:
    print("sphereA does not intersect sphereB")

  # print the largest Cube that is circumscribed by sphereA
  a = sphereA.circumscribe_cube()
  print ("Largest Cube circumscribed by sphereA: " ,a)
  print ()

  # print area of cubeA
  print ("Area of cubeA: " ,cubeA.area())

  # print volume of cubeA
  print ("Volume of cubeA: " ,cubeA.volume())

  # print if Point p is inside cubeA
  if (cubeA.is_inside_point(Point_p)):
    print ("Point p is inside cubeA")
  else:
    print("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if (cubeA.is_inside_sphere(sphereA)):
    print ("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if (cubeA.is_inside_cube(cubeB)):
    print ("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if (cubeA.is_inside_cylinder(cylA)):
    print ("cylA is inside cubeA")
  else:
    print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if (cubeA.does_intersect_cube(cubeB)):
    print ("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

  # print the intersection volume of cubeA and cubeB
  print ("Intersection volume of cubeA and cubeB: " ,cubeA.intersection_volume(cubeB))

  # print the largest Sphere object inscribed by cubeA
  print ("Largest Sphere inscribed by cubeA: " ,cubeA.inscribe_sphere())

  # print area of cylA
  print("Area of cylA: " ,cylA.area())

  # print volume of cylA
  print("Volume of cylA: " ,cylA.volume())

  # print if Point p is inside cylA
  if (cylA.is_inside_point(Point_p)):
    print ("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if (cylA.is_inside_sphere(sphereA)):
    print ("sphereA is inside cylA")
  else:
    print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  if (cylA.is_inside_cube(cubeA)):
    print ("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if (cylA.is_inside_cylinder(cylB)):
    print ("cylB is inside cylA")
  else:
    print("cylB is not inside cylA")

  # (optional) print if cylB intersects with cylA

main()