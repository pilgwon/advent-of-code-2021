input_file = open('./day01-input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# problem 1
delta_list = []
for index in range(len(input_data)):
  if index == 0:
    delta_list.append(0)
    continue
  delta = int(input_data[index]) - int(input_data[index-1])
  delta_list.append(delta)
result = len(list(filter(lambda x: x > 0, delta_list)))

# problem 2
delta_list = []
for index in range(len(input_data)-2):
  if index == 0: continue
  delta = int(input_data[index+2]) - int(input_data[index-1])
  delta_list.append(delta)
result = len(list(filter(lambda x: x > 0, delta_list)))    

print(result)
