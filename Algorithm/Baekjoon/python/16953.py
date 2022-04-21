from collections import deque
import sys
input = sys.stdin.readline
MAX_NUM = int(1e9)

def BOJ16953() :
  def bfs(initial, graph) :
    queue = deque()
    queue.append(initial)

    while queue :
      curr_node, curr_count = queue.popleft()
      next_count = curr_count + 1
      
      next_node = curr_node * 2
      if next_node <= MAX_NUM :
        if next_node not in graph or graph[next_node] > graph[curr_node] :
          graph[next_node] = next_count
          queue.append([next_node, next_count])

      next_node = int(str(curr_node) + "1")
      if next_node <= MAX_NUM : 
        if next_node not in graph or graph[next_node] > graph[curr_node]:
          graph[next_node] = next_count
          queue.append([next_node, next_count])

  A, B = map(int, input().split())
  graph = {}
  graph[A] = 0

  bfs([A, 0], graph)

  if B not in graph :
    print(-1)
    return
  
  print(graph[B] + 1)

BOJ16953()
