from collections import deque
import sys 
input = sys.stdin.readline

def BOJ2644() :
  global graph
  global visited
  global answer

  def bfs(start) :
    queue = deque()
    queue.append([start, 0])

    while queue :
      node, relation = queue.popleft()
      for i in range(len(graph[node])) :
        if visited[i] == False and graph[node][i] == 1 :
          visited[i] = True
          answer[i] = relation + 1
          queue.append([i, relation + 1])

  n = int(input())
  A, B = map(int, input().split())
  graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
  visited = [False for _ in range(n+1)]
  answer = [-1 for _ in range(n+1)]
  m = int(input())
  for _ in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

  bfs(A)
  print(answer[B])

BOJ2644()