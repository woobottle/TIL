import sys
import heapq
input = sys.stdin.readline

def BOJ1647() :
  N, M = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  visited = [False for _ in range(N+1)]

  for _ in range(M) :
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

  
  def prim() :
    result = []
    queue = []
    queue.append((0, 1))

    while queue :
      curr_cost, curr_node = heapq.heappop(queue)

      if visited[curr_node] == False :
        visited[curr_node] = True
        result.append(curr_cost)
        if len(result) == N :
          break
        for next_cost, next_node in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))

    return sum(result) - max(result)

  print(prim())

BOJ1647()
