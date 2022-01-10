import sys 
input = sys.stdin.readline

def BOJ2630() :
  global N
  global graph
  global white
  global blue

  N = int(input())
  graph = []
  white = 0
  blue = 0


  def dfs(x, y, length) :
    global N
    global graph
    global white
    global blue 

    flag = True

    for i in range(x, x + length) :
      for j in range(y, y + length) :
        if graph[x][y] != graph[i][j] and visited[i][j] == False and flag:
          flag = False
          break
    
    if flag :
      for i in range(x, x + length):
        for j in range(y, y + length):
          visited[i][j] = True
      if graph[x][y] == 0 :
        white += 1
      else :
        blue += 1

  for _ in range(N) : 
    graph.append(list(map(int, input().split())))
  visited = [[False for _ in range(N)] for _ in range(N)]
  
  length = N
  while length >= 1 :
    for i in range(0, N, length) :
      for j in range(0, N, length) :
        if visited[i][j] == False :
          dfs(i, j, length)
    length //= 2

  print(white)
  print(blue)
BOJ2630()
