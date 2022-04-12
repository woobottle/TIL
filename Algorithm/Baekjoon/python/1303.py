import sys
input = sys.stdin.readline

def BOJ1303() :
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  w_point = 0
  b_point = 0

  def bfs(x, y, letter, w_point, b_point):
    queue = []
    queue.append([x, y])
    count = 1
    visited[x][y] = True

    while queue :
      c_x, c_y = queue.pop(0)

      for dir_x, dir_y in directions:
        n_x = c_x + dir_x
        n_y = c_y + dir_y

        if 0 <= n_x < M and 0 <= n_y < N :
          if visited[n_x][n_y] == False and graph[n_x][n_y] == letter :
            visited[n_x][n_y] = True
            queue.append([n_x, n_y])
            count += 1

    if letter == "W" :
      w_point += count * count
    if letter == "B" :
      b_point += count * count

    return w_point, b_point
  N, M = map(int, input().split())
  
  graph = []
  for _ in range(M) :
    graph.append(list(input().strip()))
  visited = [[False for _ in range(N)] for _ in range(M)]
  
  for x in range(M) :
    for y in range(N) :
      if visited[x][y] == False :
        w_point, b_point = bfs(x, y, graph[x][y], w_point, b_point)

  print(w_point, b_point)

BOJ1303()


