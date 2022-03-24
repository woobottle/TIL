# import sys 
# input = sys.stdin.readline

# def BOJ2667() :
#   global graph 
#   global N
  
#   direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#   def dfs(x, y, type) :
#     stack = []
#     stack.append([x, y])
#     count = 1

#     while stack :
#       curr_x, curr_y = stack.pop()

#       for dir in direction :
#         dir_x, dir_y = dir
#         next_x = dir_x + curr_x
#         next_y = dir_y + curr_y
#         if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == False and graph[next_x][next_y] == '1':
#           visited[next_x][next_y] = type
#           count += 1
#           stack.append([next_x, next_y])
#     return count

#   N = int(input())
#   graph = []
#   for _ in range(N) :
#     graph.append(list(input().rstrip()))

#   visited = [[False for _ in range(N)] for _ in range(N)]

#   answer = 0
#   temp = {}
#   for x in range(N) :
#     for y in range(N) :
#       if graph[x][y] == '1' and visited[x][y] == False :
#         answer += 1
#         visited[x][y] = answer
#         temp[answer] = dfs(x, y, answer)

#   print(answer)
#   for i in sorted(temp.values()):
#     print(i)

# BOJ2667()

import sys 
input = sys.stdin.readline

def BOJ2667() :
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  N = int(input())
  map = []
  for _ in range(N) :
    map.append(list(input().strip()))
  
  visited = [[False for _ in range(N)] for _ in range(N)]

  def dfs(x, y):
    visited[x][y] = True
    stack = [[x, y]]
    count = 1
    
    while stack:
      curr_x, curr_y = stack.pop()

      for dir_x, dir_y in directions:
        n_x = curr_x + dir_x
        n_y = curr_y + dir_y

        if 0 <= n_x < N and 0 <= n_y < N and map[n_x][n_y] == '1':
          if visited[n_x][n_y] == False :
            count += 1
            visited[n_x][n_y] = True
            stack.append([n_x, n_y])
    return count

  result = []
  for i in range(N) :
    for j in range(N) :
      if not visited[i][j] and map[i][j] == '1' :
        result.append(dfs(i,j))

  print(len(result))
  for i in sorted(result) :
    print(i)

BOJ2667()
