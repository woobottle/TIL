import sys
input = sys.stdin.readline

def BOJ2573() :
  global N, M
  global directions

  def dfs(graph, visited, x, y) :
    stack = [[x, y]]
    while stack :
      curr_x, curr_y = stack.pop()

      for dir_x, dir_y in directions :
        next_x = curr_x + dir_x
        next_y = curr_y + dir_y
        if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] != 0 and visited[next_x][next_y] == False :
          visited[next_x][next_y] = True
          stack.append([next_x, next_y]) 

    return [graph, visited]

  def check_body_count(graph, visited) :
    count = 0
    for i in range(N) :
      for j in range(M) :
        if graph[i][j] != 0 and visited[i][j] == False :
          count += 1
          visited[i][j] = True
          graph, visited = dfs(graph, visited, i, j)
    return count
  
  def get_near_sea(graph, curr_x, curr_y) :
    count = 0 
    for dir_x, dir_y in directions :
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y
      if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 0 :
        count += 1
    return count

  def melt_with_time(graph) :
    temp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N) :
      for j in range(M) :
        if graph[i][j] != 0 :
          near_sea_count = get_near_sea(graph, i, j)
          v = graph[i][j] - near_sea_count
          if v <= 0 :
            temp[i][j] = 0
          else :
            temp[i][j] = v

          continue
        temp[i][j] = 0
    return temp

  def is_all_sea(graph) :
    is_all_sea_flag = True
    for i in range(N) :
      for j in range(M) :
        if graph[i][j] != 0 :
          is_all_sea_flag = False
          break
    return is_all_sea_flag

  N, M = map(int, input().split())
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  graph = []
  visited = [[False for _ in range(M)] for _ in range(N)]
  for _ in range(N) :
    graph.append(list(map(int, input().split())))

  count = check_body_count(graph, visited)
  if count == 0 :
    print(count)
  
  time = 0
  
  while True :
    time += 1
    melt_graph = melt_with_time(graph)
    melt_with_body = check_body_count(
        melt_graph, [[False for _ in range(M)] for _ in range(N)])
    if melt_with_body >= 2 :
      print(time)
      break
    
    if is_all_sea(melt_graph) :
      print(0)
      break
    
    graph = melt_graph
    
BOJ2573()
