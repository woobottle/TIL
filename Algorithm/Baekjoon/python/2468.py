import sys
input = sys.stdin.readline

def BOJ2468() :
  global N, temp, visited
  
  def dfs(graph, visited, x, y) :
    stack = [[x, y]]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while stack :
      curr_x, curr_y = stack.pop()

      for dir_x, dir_y in directions :
        next_x = curr_x + dir_x
        next_y = curr_y + dir_y
        if 0 <= next_x < N and 0 <= next_y < N and graph[next_x][next_y] == 1 and visited[next_x][next_y] == False :
          visited[next_x][next_y] = True
          stack.append([next_x, next_y])
    

  N = int(input())
  graph = []
  answer = []
  max_height = 0 

  for _ in range(N) :
    graph.append(list(map(int, input().split())))

  for i in range(N) :
    for j in range(N) :
      max_height = max(max_height, graph[i][j])

  for height in range(0, max_height + 1) :
    visited = [[False for _ in range(N)] for _ in range(N)]
    temp = [[1 for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N) :
      for j in range(N) :
        if graph[i][j] <= height :
          temp[i][j] = 0
    
    for i in range(N) :
      for j in range(N) :
        if temp[i][j] == 1 and visited[i][j] == False :
          count += 1
          dfs(temp, visited, i, j)

    answer.append(count)

  print(max(answer))
BOJ2468()
