def main():
  in_file = open('work.txt', 'r')
  test_cases = in_file.readline()
  test_cases_list = []
  for i in range (int(test_cases)):
    variable_list = []
    variables = in_file.readline()
    variables = variables.rstrip()
    variables = variables.split(" ")
    for j in variables:
      variable_list.append(int(j))
    test_cases_list.append(variable_list)
    n = test_cases_list[i][0]
    k = test_cases_list[i][1]
    v = (n // k)
    if (k > v):
      v = v
    elif (k < v):
      v = v - 1
    else:
      v = v
    print (n - v)
main()
