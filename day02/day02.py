input_file = open('./day02-input.txt', 'r')
input_data = input_file.read().split('\n')

# problem 1
# horizontal = 0
# vertical = 0
# for input in input_data:
#   components = input.split(' ')
#   direction = components[0]
#   units = int(components[1])
#   if direction == 'forward':
#     horizontal += units
#   elif direction == 'down':
#     vertical += units
#   elif direction == 'up':
#     vertical -= units
# result = horizontal * vertical

# problem 2
horizontalPosition = 0
depth = 0
aim = 0
for input in input_data:
  components = input.split(' ')
  direction = components[0]
  units = int(components[1])
  if direction == 'forward':
    horizontalPosition += units
    depth += aim * units
  elif direction == 'down':
    aim += units
  elif direction == 'up':
    aim -= units
result = horizontalPosition * depth

print(result)
