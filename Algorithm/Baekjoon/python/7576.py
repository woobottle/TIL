from collections import deque
import sys
input = sys.stdin.readline

RIPE = 1
UN_RIPE = 0

def BOJ7576() :
  global M, N
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  def bfs(graph) :
    queue = deque()
    temp = [[-1 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N) :
      for j in range(M) :
        if graph[i][j] == 0 :
          continue

        temp[i][j] = 0
        if graph[i][j] == 1 :
          queue.append([i, j, 0])
          visited[i][j] = True
    
    while queue :
      curr_x, curr_y, curr_day = queue.popleft()

      n_day = curr_day + 1
      for dir_x, dir_y in directions :
        n_x = curr_x + dir_x
        n_y = curr_y + dir_y
        if 0 <= n_x < N and 0 <= n_y < M and graph[n_x][n_y] == 0 and visited[n_x][n_y] == False:
          visited[n_x][n_y] = True
          queue.append([n_x, n_y, n_day])
          temp[n_x][n_y] = n_day 
          graph[n_x][n_y] = 1
    return temp

  M, N = map(int, input().split())
  graph = []
  for _ in range(N) :
    graph.append(list(map(int, input().split())))
  
  temp_graph = bfs(graph)
  day = -1
  for i in range(N) :
    for j in range(M) :
      if temp_graph[i][j] == -1 :
        print(-1)
        return
      day = max(day, temp_graph[i][j])
  
  print(day)

BOJ7576()
