#  File: Nim.py

#  Description:  This program calculates the optimum first move to win the game of nim.

#  Student's Name: Minal Kalas

#  Student's UT EID: mjk863

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 02/02/16

#  Date Last Modified: 02/03/16

#helper functions in order to get nim_sum
def nim_sum(list_nums):
  exclusive_sum = 0
  for i in list_nums:
    exclusive_sum = exclusive_sum^i
  return exclusive_sum

def nim_sum_heaps(nim_sum, list_nums):
  for i in list_nums:
    num_sum_heaps = nim_sum^i
    if num_sum_heaps< i:
      move = i - num_sum_heaps
      num_heap = list_nums.index(i)+1
      return move, num_heap

#file processing for data
def main():
  import string
  # open file for reading
  in_file =  open ("./nim.txt", "r")

  # read number of games
  num_games = in_file.readline()
  num_games = num_games.strip()
  num_games = int (num_games)

  #get heap numbers within each game and append as ints
  for i in range (num_games):
    heap_nums = in_file.readline()
    heap_nums = heap_nums.strip()
    heap_nums = heap_nums.split(" ")
    list_nums = []
    for j in (heap_nums):
      list_nums.append(int(j))

    #find nim_sum
    nim_sum_1 = nim_sum(list_nums)
    if nim_sum_1 == 0:
      print("Lose Game")
    else:
      move, num_heap = nim_sum_heaps(nim_sum_1, list_nums)
      print ("Remove "+str(move)+" counters from Heap "+str(num_heap))

  in_file.close()

main()