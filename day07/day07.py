from sys import maxsize
from functools import reduce

input_file = open('./day07-input.txt', 'r')
input_data = list(map(lambda x: int(x), input_file.read().split(',')))

# problem 1
# count = 0
# smaller = 0
# bigger = 0
# sum = reduce(lambda sum, x: sum + x, input_data, 0)
# for idx in range(max(input_data) + 1):
#   smaller = smaller + count
#   count = len(list(filter(lambda x: x == idx, input_data)))
#   bigger = len(input_data) - count - smaller
#   current = sum if idx == 0 else sum - bigger - count + smaller
#   if sum < current: break
#   sum = current
# print(sum)

# problem 2
global cahce
cache = {}
def incremental_sum(n):
  if str(n) in cache: return cache[str(n)]
  value = reduce(lambda x, y: x + y, range(n + 1))
  cache[str(n)] = value
  return value
min = maxsize
for idx in range(max(input_data) + 1):
  sum = reduce(lambda sum, input: sum + incremental_sum(abs(idx - input)), input_data, 0)
  if min < sum: break
  min = sum
print(min)
