# INF = 1e10
# import heapq
# import sys
# input = sys.stdin.readline

# def BOJ1916() :
#   N = int(input())
#   M = int(input())

#   graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

#   for _ in range(M) :
#     A, B, C = map(int, input().split())
#     graph[A][B] = min(graph[A][B], C)

#   start, end = map(int, input().split())
#   dist = [INF for _ in range(N+1)]
  
#   # 다익스트라
#   def dijkstra(start) :
#     dist[start] = 0
#     heap = []
#     heap.append([0, start])
#     while heap :
#       curr_weight, curr_node = heapq.heappop(heap)
#       if dist[curr_node] < curr_weight :
#         continue
      
#       for idx, value in enumerate(graph[curr_node]) :
#         next_weight = curr_weight + value
#         if dist[idx] > next_weight :
#           dist[idx] = next_weight
#           heapq.heappush(heap, [next_weight, idx])
  
#   dijkstra(start)      
#   print(dist[end])
# BOJ1916()
DEFAULT = 100_000_001
import sys
import heapq
input = sys.stdin.readline

def BOJ1916() :
  N = int(input())
  M = int(input())
  graph = [[DEFAULT for _ in range(N + 1)] for _ in range(N + 1)]
  for _ in range(M) :
    A, B, C = map(int, input().split())
    graph[A][B] = min(graph[A][B], C)
  
  start, end = map(int, input().split())
  
  costs = [DEFAULT for _ in range(N+1)]

  stack = []
  stack.append([0, start])
  costs[start] = 0
  while stack :
    c_cost, c_node = heapq.heappop(stack)
    for node, cost in enumerate(graph[c_node]) :
      n_cost = c_cost + cost
      if n_cost < costs[node] :
        costs[node] = n_cost
        heapq.heappush(stack, [n_cost, node])

  print(costs[end])

BOJ1916()
