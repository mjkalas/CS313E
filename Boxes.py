subsets = []

def sub_sets (a, b, idx):
  if (idx == len(a)):
    subsets.append(b)
    return
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, c, idx + 1)
    if len(b) > 1:
      if int(b[len(b) - 1][0] > b[len(b) - 2][0]):
        if int(b[len(b) - 1][1] > b[len(b) - 2][1]):
          if int(b[len(b) - 1][2] > b[len(b) - 2][2]):
            sub_sets(a, b, idx + 1)
    else:
      sub_sets (a, b, idx + 1)

def main():
  #Create an empty list of boxes
  boxes = []

  #Open and read the file boxes.txt
  in_file = open('boxes.txt', 'r')

  #Read each line of input and store in a list and sort and add to the list of boxes
  box_dimensions = []
  num_boxes = in_file.readline()
  for i in range (int(num_boxes)):
    box_dim = []
    box_num = in_file.readline()
    box_num = box_num.rstrip()
    box_num = box_num.split(" ")
    for j in box_num:
      box_dim.append(int(j))
    box_dim.sort()
    box_dimensions.append(box_dim)
  box_dimensions.sort()

  #Close the file boxes.txt
  in_file.close()

  #Get all of the subsets of boxes
  sub_sets(box_dimensions, boxes, 0)
  
  #Go through the set of nesting boxes and find the maximum
  largest = 2
  for i in subsets:
    if len(i) > largest:
      largest = len(i)

  #Print the largest set of nesting boxes
  print("Largest Subset of Nesting Boxes")
  for i in sorted(subsets):
    if len(i) == largest:
      for j in i:
        print(j)
      print()

  if largest < 2:
    print("No Nesting Boxes")

main()
