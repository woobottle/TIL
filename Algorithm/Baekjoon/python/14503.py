import sys
input = sys.stdin.readline

def BOJ14503() :
  global N, M
  global directions
  global cleared
  global graph

  def is_all_clear(r, c) :
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    flag = True
    for dir_x, dir_y in dirs :
      n_x = r + dir_x
      n_y = c + dir_y
      if 0 <= n_x < N and 0 <= n_y < M and (cleared[n_x][n_y] == 0 or graph[n_x][n_y] == 0) :
        flag = False
        break
    return flag
  
  def dfs(r, c, d) :
    stack = []
    stack.append([r, c, d])
    
    while stack :
      x, y, direction = stack.pop()
      flag = True
      for dir_x, dir_y, dir in directions[direction] :
        n_x = x + dir_x
        n_y = y + dir_y
        n_dir = dir
        if 0 <= n_x < N and 0 <= n_y < M and cleared[n_x][n_y] == 0 and graph[n_x][n_y] == 0:
          cleared[n_x][n_y] = 1
          stack.append([n_x, n_y, n_dir])
          flag = False
          break
      
      if flag :
        back_x, back_y, _ = directions[direction][1]
        n_x = back_x + x
        n_y = back_y + y
        if graph[n_x][n_y] != 1 :
          stack.append([x + back_x, y + back_y, direction])
  
  N, M = map(int, input().split())
  r, c, d = map(int, input().split())
  
  directions = {
    0: [[0, -1, 3], [1, 0, 2], [0, 1, 1], [-1, 0, 0]], 
    1: [[-1, 0, 0], [0, -1, 3], [1, 0, 2], [0, 1, 1]],
    2: [[0, 1, 1], [-1, 0, 0], [0, -1, 3], [1, 0, 2]], 
    3: [[1, 0, 2], [0, 1, 1], [-1, 0, 0], [0, -1, 3]]
  }

  graph = []
  cleared = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(N) :
    graph.append(list(map(int, input().split())))

  cleared[r][c] = 1
  dfs(r, c, d)
  
  count = 0
  for i in range(N - 1) :
    for j in range(M - 1) :
      if cleared[i][j] == 1 :
        count += 1
  print(count)

BOJ14503()
