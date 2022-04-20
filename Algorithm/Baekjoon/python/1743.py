from collections import deque
import sys
input = sys.stdin.readline

def BOJ1743() :
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  
  def bfs(x, y, map) :
    count = 1
    queue = deque()
    queue.append([x, y])

    while queue :
      curr_x, curr_y = queue.popleft()

      for dir_x, dir_y in directions :
        next_x = curr_x + dir_x
        next_y = curr_y + dir_y

        if 0 <= next_x < N and 0 <= next_y < M :
          if visited[next_x][next_y] == False and map[next_x][next_y] == 1 :
            count += 1
            visited[next_x][next_y] = True
            queue.append([next_x, next_y])

    return count

  N, M, K = map(int, input().split())

  graph = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(K) :
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

  visited = [[False for _ in range(M)] for _ in range(N)]
  result = 0
  
  for r in range(N) :
    for c in range(M) :
      if visited[r][c] == False and graph[r][c] == 1 :
        visited[r][c] = True
        result = max(result, bfs(r,c, graph))

  print(result)
BOJ1743()
