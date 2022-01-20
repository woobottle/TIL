from collections import deque
import sys
input = sys.stdin.readline


def BOJ1260():
  def dfs(start, visited, graph):
    stack = []
    stack.append(start)
    print(start, end=" ")

    while stack:
      node = stack.pop()
      visited[node] = True

      for next in range(1, len(graph[node])):
        if visited[next] == False and graph[node][next] == 1:
          visited[next] = True
          dfs(next, visited, graph)

  def bfs(start, visited, graph):
    queue = deque()
    queue.append(start)

    while queue:
      node = queue.popleft()
      visited[node] = True
      print(node, end=" ")

      for next in range(1, len(graph[node])):
        if visited[next] == False and graph[node][next] == 1:
          visited[next] = True
          queue.append(next)

  N, M, V = map(int, input().split())
  graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
  for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

  visited = [False for _ in range(N+1)]
  dfs(V, visited, graph)

  print()

  visited = [False for _ in range(N+1)]
  bfs(V, visited, graph)


BOJ1260()
