import sys
input = sys.stdin.readline
directions = [[1,0], [-1,0], [0,1], [0,-1]] 

def findOtherSwan(array, first_swan, second_swan) :
  stack = []
  stack.append(first_swan)
  isRouteOpen = False
  height = len(array)
  width = len(array[0])
  visited = [[0] * width for _ in range(height)]

  second_swan_x, second_swan_y = second_swan

  while stack :
    curr_x, curr_y = stack.pop()

    for dir in directions : 
      dir_x, dir_y = dir
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y

      if next_x < 0 or height <= next_x or next_y < 0 or width <= next_y :
        continue
      
      if visited[next_x][next_y] or array[next_x][next_y] == 'X':
        continue
      
      if array[next_x][next_y] == '.':
        visited[next_x][next_y] = 1
        stack.append([next_x, next_y])

      if next_x == second_swan_x and next_y == second_swan_y :
        isRouteOpen = True
        while stack :
          stack.pop()
        break

  return isRouteOpen

def deleteIce(array, ice_array) :
  need_delete_ices = []
  height = len(array)
  width = len(array[0])

  for ice in ice_array :
    ice_x, ice_y = ice
    
    for dir in directions : 
      dir_x, dir_y = dir
      check_x = ice_x + dir_x
      check_y = ice_y + dir_y

      if check_x < 0 or height <= check_x or check_y < 0 or width <= check_y:
        continue
      
      if array[check_x][check_y] == "." :
        need_delete_ices.append([ice_x, ice_y])
        break
  
  for ice in need_delete_ices :
    ice_x, ice_y = ice
    array[ice_x][ice_y] = "."
    ice_array.remove(ice)

  return [array, ice_array]

def BOJ3197():
  R, C = map(int, input().split())
  graph = []
  swans = []
  ices = []
  time = 0

  for _ in range(R) :
    graph.append(list(input().strip()))
  
  for x in range(R) :
    for y in range(C) :
      if graph[x][y] == 'L' :
        swans.append([x,y])
      if graph[x][y] == 'X' :
        ices.append([x,y])

  while True :
    isRouteOpen = findOtherSwan(graph, swans[0], swans[1])

    if isRouteOpen :
      print(time)
      break

    graph, ices = deleteIce(graph, ices)
    time += 1
  

BOJ3197()

# https://rebas.kr/780
