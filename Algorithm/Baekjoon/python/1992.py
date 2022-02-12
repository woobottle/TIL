import sys
input = sys.stdin.readline

def BOJ1992() :
  global graph
  
  def check(x, y, step) :
    flag = True
    pivot = graph[x][y]
    
    for i in range(x, x + step) :
      for j in range(y, y + step) :
        if graph[i][j] != pivot :
          flag = False
          break
    
    if flag == False :
      print("(", end='')
      step //= 2
      check(x, y, step)
      check(x, y+step, step)
      check(x+step, y, step)
      check(x+step, y+step, step)
      print(")", end='')
    elif pivot == '1' :
      print(1, end='')
    else :
      print(0, end='')
    
  N = int(input())
  step = int(N)
  
  graph = []
  for _ in range(N) :
    graph.append(list(input().rstrip()))
  
  check(0, 0, step)

BOJ1992()
