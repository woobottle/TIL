import sys 
input = sys.stdin.readline

def BOJ2667() :
  global graph 
  global N
  
  direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  def dfs(x, y, type) :
    stack = []
    stack.append([x, y])
    count = 1

    while stack :
      curr_x, curr_y = stack.pop()

      for dir in direction :
        dir_x, dir_y = dir
        next_x = dir_x + curr_x
        next_y = dir_y + curr_y
        if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == False and graph[next_x][next_y] == '1':
          visited[next_x][next_y] = type
          count += 1
          stack.append([next_x, next_y])
    return count

  N = int(input())
  graph = []
  for _ in range(N) :
    graph.append(list(input().rstrip()))

  visited = [[False for _ in range(N)] for _ in range(N)]

  answer = 0
  temp = {}
  for x in range(N) :
    for y in range(N) :
      if graph[x][y] == '1' and visited[x][y] == False :
        answer += 1
        visited[x][y] = answer
        temp[answer] = dfs(x, y, answer)

  print(answer)
  for i in sorted(temp.values()):
    print(i)

BOJ2667()
