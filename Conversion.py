def main():
  dict_data = []
  dictionary = {}
  out_file = open("formatted_data.txt", "w")
  in_file = open('flight_data.txt', 'r')
  box_dimensions = []
  num_flights = in_file.readline()
  for i in range (int(num_flights)):
    box_dim = []
    box_num = in_file.readline()
    box_num = box_num.strip()
    box_num = box_num.split(",")
    print(len(box_num))
    if (len(box_num) != 1):
      key, value = box_num[0], box_num[1]
      key, value = box_num[2], box_num[3]
      key, value = box_num[4], box_num[5]
      key, value = box_num[6], box_num[7]
      key, value = box_num[8], box_num[9]
      key, value = box_num[10], box_num[11]
      key, value = box_num[12], box_num[13]
      key, value = box_num[14], box_num[15]
      key, value = box_num[16], box_num[17]
      key, value = box_num[18], box_num[19]
      dictionary[key] = value
    out_file.write(str(dictionary))
  #out_file.write(str(dict_data))
  out_file.close()
  in_file.close()

main()