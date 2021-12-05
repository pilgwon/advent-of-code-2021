input_file = open('./day04-input.txt', 'r')
input_data = input_file.read().split('\n')

def check_bingo(check):
  bingo_size = 5
  for index in range(bingo_size):
    row = bingo_size * index
    if check[row+0] and check[row+1] and check[row+2] and check[row+3] and check[row+4]:
      return True
    if check[index] and check[bingo_size+index] and check[bingo_size*2+index] and check[bingo_size*3+index] and check[bingo_size*4+index]:
      return True

def calculate_score(bingo, check, number):
  sum = 0
  for index in range(len(check)):
    if check[index] == False:
      sum += int(bingo[index])
  return sum * int(number)

bingo_index = 0
number_of_bingos = int((len(input_data) - 1) / 6)
bingos = [[] for i in range(number_of_bingos)]
checks = [[False for j in range(25)] for i in range(number_of_bingos)]
for index in range(2, len(input_data)):
  if input_data[index] == '':
    bingo_index += 1
    continue
  bingos[bingo_index].extend(input_data[index].split())

# problem 1
# result = 0
# is_bingo = False
# for number in input_data[0].split(','):
#   for index in range(len(bingos)):
#     bingo = bingos[index]
#     idx = bingo.index(number) if number in bingo else None
#     if idx != None:
#       checks[index][idx] = True
#     is_bingo = check_bingo(checks[index])
#     if is_bingo:
#       result = calculate_score(bingo, checks[index], number)
#       break
#   if is_bingo: break

# problem 2
result = 0
is_bingo = [False for i in range(number_of_bingos)]
for number in input_data[0].split(','):
  for index in range(len(bingos)):
    if is_bingo[index] == True: continue
    bingo = bingos[index]
    idx = bingo.index(number) if number in bingo else None
    if idx != None: checks[index][idx] = True
    is_bingo[index] = check_bingo(checks[index])
    if is_bingo[index]:
      result = calculate_score(bingo, checks[index], number)
  if len(list(filter(lambda x: x == True, is_bingo))) == number_of_bingos: break

print(result)
