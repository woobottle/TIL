from collections import deque
import sys 

def BOJ1797() :
  def bfs(start) :
    bi[start] = 1
    queue = deque()
    queue.append(start)
    while queue :
      curr = queue.popleft()
      for i in graph[curr] :
        if bi[i] == 0 :
          bi[i] = -bi[curr]
          queue.append(i)
        else :
          if bi[i] == bi[curr] :
            return False
    return True

  k = int(sys.stdin.readline())
  for _ in range(k) :
    global graph
    global flag
    global bi
    global queue

    flag = "YES"
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    bi = [0 for _ in range(V+1)]
    for _ in range(E) :
      u, v = map(int, sys.stdin.readline().split())
      graph[u].append(v)
      graph[v].append(u)

    for k in range(1, V+1) :
      if bi[k] == 0 :
        if not bfs(k) :
          flag = "NO"
          break
        
    print(flag)

BOJ1797()

# https://pacific-ocean.tistory.com/349
