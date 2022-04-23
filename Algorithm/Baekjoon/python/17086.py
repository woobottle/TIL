from collections import deque
import sys
input = sys.stdin.readline

def BOJ17086() :
  directions = [[1, 0], [1, -1], [0, -1],
                [-1, -1], [-1, 0], [-1, 1], [1, 1], [0, 1]]
  
  N, M = map(int, input().split())
  graph = []
  for _ in range(N) :
    graph.append(list(map(int, input().split())))
  distances = []

  def bfs(x, y, start) :
    temp = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True
    
    queue = deque()
    queue.append([x, y, start])

    while queue :
      curr_x, curr_y, curr_distance = queue.popleft()
      next_distance = curr_distance + 1

      for dir_x, dir_y in directions :
        next_x = curr_x + dir_x
        next_y = curr_y + dir_y

        if next_x < 0 or N <= next_x or next_y < 0 or M <= next_y :
          continue

        if graph[next_x][next_y] == 0 and visited[next_x][next_y] == False:
          queue.append([next_x, next_y, next_distance])
          visited[next_x][next_y] = True

        if graph[next_x][next_y] == 1 and visited[next_x][next_y] == False:
          temp.append(next_distance)
          break

    distances.append(min(temp))

  for x in range(N) :
    for y in range(M) :
      if graph[x][y] == 0 :
        bfs(x, y, 0)

  print(max(distances))
BOJ17086()

# 어떤 칸의 안전거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다.
# 여러마리의 아기상어들 중 거리가 가장 가까운 상어들과의 거리중 최댓값을 구하라
# 이동은 8방향으로 가능 
# [[1, 0], [1, -1], [0, -1], [-1, -1],
#  [-1, 0], [-1, 1], [1, 1], [0, 1]]
