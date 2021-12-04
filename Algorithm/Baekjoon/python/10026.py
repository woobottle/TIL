import sys 

directions = [[0, 1],[0, -1], [-1, 0], [1, 0]]

def color_check(array, visited, location, colors) :
  x, y = location
  queue = []
  queue.append([x,y])
  while queue :
    curr_x, curr_y = queue.pop(0)
    for direction in directions :
      dir_x, dir_y = direction
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y
      if 0 <= next_x < len(array) and 0 <= next_y < len(array) and visited[next_x][next_y] == 0 and array[next_x][next_y] in colors:
        visited[next_x][next_y] = 1
        queue.append([next_x, next_y])
  return visited

n = int(input())
array = []
for _ in range(n) :
  line = sys.stdin.readline().strip()
  array.append(list(line))

normal_count = 0
un_normal_count = 0

visited = [[0] * n for _ in range(n)]
color_type = ['R', 'G', 'B']
for color in color_type :
  for i in range(n) :
    for j in range(n) :
      if visited[i][j] == 0 and array[i][j] in color :
        visited[i][j] = 1
        visited = color_check(array, visited, [i,j], color)
        normal_count += 1

visited = [[0] * n for _ in range(n)]
color_type = ['RG', 'B']
for color in color_type :
  for i in range(n) :
    for j in range(n) :
      if visited[i][j] == 0 and array[i][j] in color :
        visited[i][j] = 1
        visited = color_check(array, visited, [i,j], color)
        un_normal_count += 1


print(normal_count, un_normal_count)
