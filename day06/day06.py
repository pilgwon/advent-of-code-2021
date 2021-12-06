input_file = open('./day06-input.txt', 'r')
input_data = input_file.read().split(',')

global default_creation
default_creation = 7
global new_creation
new_creation = 9
global cache
cache = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1}

def calculate(x, y):
  if str(x) in cache: return cache[str(x)]
  x -= y
  sum = 0
  while(x >= 0):
    value = calculate(x, new_creation)
    cache[str(x)] = value
    sum += value
    x -= default_creation
  return sum + 1

# problem 1
# cache = {}
# result = 0
# for input in input_data:
#   if input not in cache:
#     cache[input] = calculate(80, int(input)+1)
#   result += cache[input]

# problem 2
result = 0
result_cache = {}
for input in input_data:
  if input not in result_cache:
    result_cache[input] = calculate(256, int(input)+1)
  result += result_cache[input]

print(result)
