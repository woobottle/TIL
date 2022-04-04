import sys
input = sys.stdin.readline

def BOJ3085() :
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  def getMaxiMumCandy(arr) :
    n = len(arr)
    answer = 1
    for i in range(n) :
      cnt = 1
      for j in range(1, n) :
        if arr[i][j] == arr[i][j-1] :
          cnt += 1
        else :
          cnt = 1
        answer = max(answer, cnt)
    
      cnt = 1
      for j in range(1, n) :
        if arr[j][i] == arr[j-1][i] :
          cnt += 1
        else :
          cnt = 1
        answer = max(answer, cnt)
    return answer

  N = int(input())
  graph = []
  for _ in range(N) :
    graph.append(list(input().strip()))
  
  result = 0
  for x in range(N) :
    for y in range(N) :
      for d_x, d_y in directions :
        n_x = x + d_x
        n_y = y + d_y
        if 0 <= n_x < N and 0 <= n_y < N :
          if graph[x][y] != graph[n_x][n_y] :
            graph[n_x][n_y], graph[x][y] = graph[x][y], graph[n_x][n_y]
            result = max(result, getMaxiMumCandy(graph))
            graph[x][y], graph[n_x][n_y] = graph[n_x][n_y], graph[x][y]

  print(result)
BOJ3085()
