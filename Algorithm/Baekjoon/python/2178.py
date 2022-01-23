import sys
input = sys.stdin.readline
INF = 1e9

def BOJ2178() :
  global graph 
  global result 
  global N, M
  
  def dfs(x, y, count) :
    stack = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result[x][y] = count 
    stack.append([x, y, count])

    while stack :
      curr_x, curr_y, curr_count = stack.pop()

      for dir_x, dir_y in directions :
        next_x = curr_x + dir_x 
        next_y = curr_y + dir_y
        next_count = curr_count + 1
        
        if 0 <= next_x < N and 0 <= next_y < M :
          if result[next_x][next_y] > next_count and graph[next_x][next_y] == '1':
            stack.append([next_x, next_y, next_count])
            result[next_x][next_y] = next_count

  N, M = map(int, input().split())
  graph = []
  result = [[INF for _ in range(M)] for _ in range(N)]
  for _ in range(N) :
    graph.append(list(input().rstrip()))
  
  dfs(0, 0, 1)
  print(result[N-1][M-1])

BOJ2178()
