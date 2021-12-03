from functools import reduce

input_file = open('./day03-input.txt', 'r')
input_data = input_file.read().split('\n')

# problem 1
# count = [0 for i in range(len(input_data[0]))]
# for input in input_data:
#   for index in range(len(input)):
#     count[index] += 1 if input[index] == '0' else -1
# def process(x):
#   return int(''.join(list(x)), 2)
# gamma = process(map(lambda x: '1' if x > 0 else '0', count))
# epsilon = process(map(lambda x: '1' if x < 0 else '0', count))
# result = gamma * epsilon

# problem 2
def bitAsDelta(bit): return 1 if bit == '1' else -1
def determine(candidates, deltaAsBit):
  for index in range(len(candidates[0])):
    if len(candidates) == 1: break
    common = reduce(lambda acc, cur: acc + bitAsDelta(cur[index]), candidates, 0)
    candidates = list(filter(lambda x: x[index] == deltaAsBit(common), candidates))
  return int(candidates[0], 2)
def oxygen(candidates):
  def deltaAsBit(delta): return '0' if delta < 0 else '1'
  return determine(candidates, deltaAsBit)
def co2(candidates):
  def deltaAsBit(delta): return '1' if delta < 0 else '0'
  return determine(candidates, deltaAsBit)
result = oxygen(input_data) * co2(input_data)

print(result)
