input_file = open('./day05-input.txt', 'r')
input_data = input_file.read().split('\n')

def check_at(pos, check):
  if pos not in check: check[pos] = 1
  else: check[pos] += 1

# problem 1
# check = {}
# for input in input_data:
#   leftX, leftY = list(map(int, input.split(' -> ')[0].split(',')))
#   rightX, rightY = list(map(int, input.split(' -> ')[1].split(',')))
#   if leftX == rightX:
#     stop = max(leftY, rightY) + 1
#     start = min(leftY, rightY)
#     for y in range(start, stop):
#       check_at('(%s, %s)' % (leftX, y), check)
#   elif leftY == rightY:
#     stop = max(leftX, rightX) + 1
#     start = min(leftX, rightX)
#     for x in range(start, stop):
#       check_at('(%s, %s)' % (x, leftY), check)
# result = 0
# for key in check.keys():
#   if check[key] >= 2: result += 1

# problem 2
check = {}
for input in input_data:
  leftX, leftY = list(map(int, input.split(' -> ')[0].split(',')))
  rightX, rightY = list(map(int, input.split(' -> ')[1].split(',')))
  if leftX == rightX:
    stop = max(leftY, rightY) + 1
    start = min(leftY, rightY)
    for y in range(start, stop):
      check_at('(%s, %s)' % (leftX, y), check)
  elif leftY == rightY:
    stop = max(leftX, rightX) + 1
    start = min(leftX, rightX)
    for x in range(start, stop):
      check_at('(%s, %s)' % (x, leftY), check)
  elif abs(leftX - rightX) == abs(leftY - rightY):
    x = leftX
    y = leftY
    endX = rightX-1 if leftX > rightX else rightX + 1
    endY = rightY-1 if leftY > rightY else rightY + 1
    while(1):
      check_at('(%s, %s)' % (x, y), check)
      if x == rightX and y == rightY: break
      x = x+1 if x < rightX else x-1
      y = y+1 if y < rightY else y-1
result = 0
for key in check.keys():
  if check[key] >= 2: result += 1


print(result)
