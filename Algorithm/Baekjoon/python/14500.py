def BOJ14500() :
  global result
  n,m = map(int, input().split())
  graph = []
  for _ in range(n) :
    graph.append(list(map(int, input().split())))
  visited = [[0] * m for _ in range(n)]
  direction = [[0,1], [0,-1], [1,0], [-1,0]]
  result = 0
  middle_finger_tetromino = [[[0,1], [0,2], [1,1]], [
      [0,1], [0,2], [-1,1]], [[1,0], [2,0], [1,1]], [[1,0], [2,0], [1,-1]]]

  def dfs(x, y, count, number, visited):
    global result
    if count == 4 :
      result = max(result, number)
      return
    for dir in direction:
      dir_x, dir_y = dir
      next_x = dir_x + x
      next_y = dir_y + y
      if 0 <= next_x < n and 0 <= next_y < m and visited[next_x][next_y] == 0:
        visited[next_x][next_y] = 1
        dfs(next_x, next_y, count+1, number + graph[next_x][next_y], visited)
        visited[next_x][next_y] = 0
    
  def middle_finger(x, y) :
    global result
    for tetromino in middle_finger_tetromino :
      flag = True
      temp = graph[x][y]
      for dir in tetromino :
        dir_x, dir_y = dir
        next_x = x + dir_x
        next_y = y + dir_y
        if 0 <= next_x < n and 0 <= next_y < m :
          temp += graph[next_x][next_y]
        else :
          flag = False
          break
      if flag :
        result = max(result, temp)

  for x in range(n) :
    for y in range(m) :
      visited[x][y] = 1
      dfs(x, y, 1, graph[x][y], visited)
      visited[x][y] = 0
      middle_finger(x, y)

  print(result)

BOJ14500()


# https://pacific-ocean.tistory.com/364